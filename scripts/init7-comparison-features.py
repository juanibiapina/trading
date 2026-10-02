#!/usr/bin/env python3
"""Replay frozen Initiative 7 price features; archive evidence without orders, model calls or portfolios."""

import argparse
import datetime as dt
import hashlib
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo

from volume_metric import timestamp


def sha(data):
    return hashlib.sha256(data).hexdigest()


def features(source, design):
    if design['version'] != 'init7-comparison-v1':
        raise ValueError('Unknown comparison design')
    basket = design['basket']
    if source['version'] != 'init7-data-census-v1' or source['symbols'] != basket:
        raise ValueError('Capture must use the frozen basket')
    slot = dt.timedelta(minutes=design['bar_timeframe_minutes'])
    lookback = dt.timedelta(minutes=design['lookback_minutes'])
    count = design['required_consecutive_closes']
    if lookback != slot * (count - 1):
        raise ValueError('Lookback and consecutive close count disagree')
    bars_source = source['current_delayed_sip']
    if (bars_source['feed'], bars_source['timeframe'], bars_source['adjustment']) != ('sip', '5Min', 'raw'):
        raise ValueError('Explicit raw SIP five-minute input required')
    if not bars_source['pages'] or bars_source['pages'][-1]['payload'].get('next_page_token'):
        raise ValueError('Incomplete SIP pagination')
    decision = timestamp(source['iex_quotes']['received_utc'])
    receipts = [source[key]['received_utc'] for key in ('clock', 'calendar')]
    receipts += [page['received_utc'] for page in bars_source['pages']]
    if any(timestamp(value) > decision for value in receipts):
        raise ValueError('An input arrived after the reference decision cutoff')
    if timestamp(source['clock']['payload']['timestamp']) > decision:
        raise ValueError('Market clock is ahead of the decision cutoff')
    zone = ZoneInfo(design['time_zone'])
    calendar = source['current_session']
    day = dt.date.fromisoformat(calendar['date'])
    opened, closed = (dt.datetime.combine(day, dt.time.fromisoformat(calendar[key]), zone)
                      .astimezone(dt.timezone.utc) for key in ('open', 'close'))
    if not opened <= decision < closed:
        raise ValueError('Reference observation is outside the regular session')
    cutoff = min(timestamp(bars_source['end_utc']), closed,
                 timestamp(source['clock']['payload']['timestamp'])
                 - dt.timedelta(minutes=design['request_buffer_minutes']))
    slot_count = max(0, int((cutoff - opened) // slot))
    latest_start = opened + slot * (slot_count - 1) if slot_count else None
    required = ([latest_start - slot * i for i in reversed(range(count))]
                if slot_count >= count else [])
    indexed = {symbol: {} for symbol in basket}
    for page in bars_source['pages']:
        for symbol, bars in page['payload'].get('bars', {}).items():
            if symbol not in indexed:
                continue
            for bar in bars:
                stamp = timestamp(bar['t'])
                if stamp in indexed[symbol]:
                    raise ValueError(f'Duplicate {symbol} bar at {stamp.isoformat()}')
                indexed[symbol][stamp] = bar
    result = {
        'decision_cutoff_utc': decision.isoformat(), 'feature_cutoff_utc': cutoff.isoformat(),
        'last_complete_end_utc': (latest_start + slot).isoformat() if latest_start else None,
        'required_bar_starts_utc': [value.isoformat() for value in required],
        'scheduled_observation': decision.astimezone(zone).strftime('%H:%M') in design['observation_times_et'],
        'rows': [], 'numerical_candidate': None, 'reason': None,
        'book_diagnostic': None,
        'limit': 'Feature/interface replay only; pre-decision IEX quote is not an entry fill. No Jev decision, portfolio or prospective return.'
    }
    returns = {}
    for symbol in basket:
        missing = [value.isoformat() for value in required if value not in indexed[symbol]]
        closes = [indexed[symbol][value]['c'] for value in required if value in indexed[symbol]]
        if any(type(value) not in (int, float) or not math.isfinite(value) or value <= 0 for value in closes):
            raise ValueError(f'Invalid {symbol} close')
        value = closes[-1] / closes[0] - 1 if required and not missing else None
        returns[symbol] = value
        result['rows'].append({'symbol': symbol, 'missing_utc': missing,
                               'observed_required_closes': len(closes), 'return_30m_pct': value * 100 if value is not None else None})
    if not required or any(value is None for value in returns.values()):
        result['reason'] = 'missing_exact_basket_window'
        return result
    market = returns[design['market_comparator']]
    ranked = sorted(design['tradable_candidates'], key=lambda symbol: (-(returns[symbol] - market), symbol))
    result['ranking'] = [{'symbol': symbol, 'relative_return_pct_points': (returns[symbol] - market) * 100} for symbol in ranked]
    selected = ranked[0]
    if returns[selected] <= 0 or returns[selected] - market <= 0:
        result['reason'] = 'no_positive_absolute_and_relative_return'
        return result
    result.update(numerical_candidate=selected, reason='positive_absolute_and_relative_return')
    quote = source['iex_quotes']['payload'].get('quotes', {}).get(selected, {})
    age = (decision - timestamp(quote['t'])).total_seconds() if quote.get('t') else None
    bid, ask, bs, ass = (quote.get(key, 0) for key in ('bp', 'ap', 'bs', 'as'))
    valid = all(type(value) in (int, float) and math.isfinite(value) for value in (bid, ask, bs, ass))
    fresh = bool(valid and bid > 0 and ask >= bid and bs > 0 and ass > 0
                 and age is not None and 0 <= age <= design['future_pilot_execution']['quote_max_age_seconds'])
    result['book_diagnostic'] = {'quote_utc': quote.get('t'), 'received_utc': decision.isoformat(),
                                 'bid': bid, 'ask': ask, 'bid_size': bs, 'ask_size': ass,
                                 'age_seconds': age, 'fresh_two_sided': fresh,
                                 'fractional_asset_check': 'required separately',
                                 'post_decision_entry_quote': False}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--design', type=Path, required=True)
    parser.add_argument('--input', type=Path, required=True, help='Archived census; no network access')
    parser.add_argument('--output', type=Path, required=True, help='New immutable reference artifact')
    args = parser.parse_args()
    design_bytes, source_bytes = args.design.read_bytes(), args.input.read_bytes()
    result = features(json.loads(source_bytes), json.loads(design_bytes))
    record = {'version': 'init7-comparison-features-v1', 'mode': 'development_reference_excluded_from_prospective_performance',
              'generated_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
              'design_path': str(args.design), 'design_sha256': sha(design_bytes),
              'input_path': str(args.input), 'input_sha256': sha(source_bytes),
              'selector_sha256': sha(Path(__file__).read_bytes()), 'result': result}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as target:
        json.dump(record, target, indent=2, allow_nan=False)
        target.write('\n')
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
