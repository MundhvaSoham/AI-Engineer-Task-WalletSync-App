import dateparser
from datetime import datetime, timedelta
import re
from typing import Optional, Dict

def parse_time_range(text: str) -> Optional[Dict[str, str]]:
    text = text.lower()
    now = datetime.now()

    # Common expressions
    if 'last month' in text:
        first = (now.replace(day=1) - timedelta(days=1)).replace(day=1)
        last = now.replace(day=1) - timedelta(days=1)
        return {'start': first.strftime('%Y-%m-%d'), 'end': last.strftime('%Y-%m-%d')}
    if 'this month' in text:
        first = now.replace(day=1)
        last = now
        return {'start': first.strftime('%Y-%m-%d'), 'end': last.strftime('%Y-%m-%d')}
    if 'last week' in text:
        start = now - timedelta(days=now.weekday() + 7)
        end = start + timedelta(days=6)
        return {'start': start.strftime('%Y-%m-%d'), 'end': end.strftime('%Y-%m-%d')}
    if 'this week' in text:
        start = now - timedelta(days=now.weekday())
        end = now
        return {'start': start.strftime('%Y-%m-%d'), 'end': end.strftime('%Y-%m-%d')}
    if 'last 7 days' in text or 'past 7 days' in text:
        start = now - timedelta(days=7)
        end = now
        return {'start': start.strftime('%Y-%m-%d'), 'end': end.strftime('%Y-%m-%d')}
    if 'last 30 days' in text or 'past 30 days' in text:
        start = now - timedelta(days=30)
        end = now
        return {'start': start.strftime('%Y-%m-%d'), 'end': end.strftime('%Y-%m-%d')}

    # Month and year (e.g., "April 2024")
    m = re.search(r'(january|february|march|april|may|june|july|august|september|october|november|december) (\d{4})', text)
    if m:
        month = m.group(1)
        year = int(m.group(2))
        dt = dateparser.parse(f'1 {month} {year}')
        if dt:
            next_month = dt.replace(day=28) + timedelta(days=4)
            last_day = next_month - timedelta(days=next_month.day)
            return {'start': dt.strftime('%Y-%m-%d'), 'end': last_day.strftime('%Y-%m-%d')}

    # Between X and Y
    m = re.search(r'between (.+?) and (.+)', text)
    if m:
        start = dateparser.parse(m.group(1))
        end = dateparser.parse(m.group(2))
        if start and end:
            return {'start': start.strftime('%Y-%m-%d'), 'end': end.strftime('%Y-%m-%d')}

    # Fallback: try to parse any date range
    dates = list(dateparser.search.search_dates(text)) if hasattr(dateparser, 'search') else []
    if len(dates) >= 2:
        return {'start': dates[0][1].strftime('%Y-%m-%d'), 'end': dates[1][1].strftime('%Y-%m-%d')}

    return None

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        text = input('Enter time expression: ')
    result = parse_time_range(text)
    print(result) 