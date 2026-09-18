#!/usr/bin/env bash
set -u

max_attempts=10

for attempt in $(seq 1 "$max_attempts"); do
  if [ -e .git/index.lock ]; then
    if [ "$attempt" -eq "$max_attempts" ]; then
      printf 'git sync: .git/index.lock remained after %d attempts\n' "$max_attempts" >&2
      exit 1
    fi
    sleep 2
    continue
  fi

  stash_output=$(git stash 2>&1)
  stash_status=$?
  printf '%s\n' "$stash_output"
  if [ "$stash_status" -ne 0 ]; then
    case "$stash_output" in
      *index.lock*)
        if [ "$attempt" -lt "$max_attempts" ]; then
          sleep 2
          continue
        fi
        ;;
    esac
    exit "$stash_status"
  fi

  pull_output=$(git pull --ff-only 2>&1)
  pull_status=$?
  printf '%s\n' "$pull_output"
  if [ "$pull_status" -ne 0 ]; then
    git stash pop 2>/dev/null || true
    case "$pull_output" in
      *index.lock*)
        if [ "$attempt" -lt "$max_attempts" ]; then
          sleep 2
          continue
        fi
        ;;
    esac
    exit "$pull_status"
  fi

  git stash pop 2>/dev/null || true
  exit 0
done
