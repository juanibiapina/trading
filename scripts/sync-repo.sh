#!/usr/bin/env bash
set -u

max_attempts=10

# Scheduled sessions that resume together after a provider outage run this
# script at the same second. Overlapping `git pull` fetches append to
# FETCH_HEAD, and with pull.rebase=true Git then fails with
# "Cannot rebase onto multiple branches". Hold one lock for the whole sync so
# concurrent callers take turns.
git_dir=$(git rev-parse --git-dir) || exit 1
exec 9>"$git_dir/sync-repo.lock"
if ! flock -w 120 9; then
  printf 'git sync: another sync held %s/sync-repo.lock for 120s\n' "$git_dir" >&2
  exit 1
fi

# Errors caused by another Git process touching the repo at the same time.
is_transient() {
  case "$1" in
    *index.lock*|*"Cannot rebase onto multiple branches"*|*"cannot lock ref"*) return 0 ;;
  esac
  return 1
}

for attempt in $(seq 1 "$max_attempts"); do
  if [ -e "$git_dir/index.lock" ]; then
    if [ "$attempt" -eq "$max_attempts" ]; then
      printf 'git sync: %s/index.lock remained after %d attempts\n' "$git_dir" "$max_attempts" >&2
      exit 1
    fi
    sleep 2
    continue
  fi

  stash_output=$(git stash 2>&1)
  stash_status=$?
  printf '%s\n' "$stash_output"
  if [ "$stash_status" -ne 0 ]; then
    if is_transient "$stash_output" && [ "$attempt" -lt "$max_attempts" ]; then
      sleep 2
      continue
    fi
    exit "$stash_status"
  fi
  # Pop only what this run stashed; a bare pop would apply an older stash.
  case "$stash_output" in
    *"No local changes to save"*) pop_stash() { :; } ;;
    *) pop_stash() { git stash pop 2>/dev/null || true; } ;;
  esac

  pull_output=$(git pull --ff-only 2>&1)
  pull_status=$?
  printf '%s\n' "$pull_output"
  if [ "$pull_status" -ne 0 ]; then
    pop_stash
    if is_transient "$pull_output" && [ "$attempt" -lt "$max_attempts" ]; then
      sleep 2
      continue
    fi
    exit "$pull_status"
  fi

  pop_stash
  exit 0
done
