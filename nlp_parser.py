import re
import json
from typing import Optional, Dict
from time_parser import parse_time_range
from fuzzy_category import resolve_category

# Basic category mapping for demo
CATEGORIES = [
    'food', 'entertainment', 'transport', 'shopping', 'bills', 'health', 'salary', 'investment', 'gift', 'other'
]

# Intent patterns (expand as needed)
INTENT_PATTERNS = [
    (r'(income vs expense|income versus expense|compare income and expense)', 'income_vs_expense'),
    (r'(spend|spent|expense|expenses) on (?P<category>\w+)', 'category_expense'),
    (r'(highest spending|most spent|top category)', 'top_category'),
    (r'(daily expenses|expenses per day|day wise expenses)', 'daily_expenses'),
    (r'(income|earned|salary)', 'income'),
    (r'(expense|spent|spending)', 'expense'),
]

def extract_category(text: str) -> Optional[str]:
    for cat in CATEGORIES:
        if cat in text.lower():
            return cat
    return None

def parse_intent_and_entities(query: str) -> Dict:
    query_lc = query.lower()
    result = {}
    # Intent detection
    for pattern, intent in INTENT_PATTERNS:
        match = re.search(pattern, query_lc)
        if match:
            result['intent'] = intent
            # Category extraction
            if 'category' in match.groupdict():
                cat = resolve_category(match.group('category'))
                if cat:
                    result['category'] = cat
            else:
                cat = resolve_category(query_lc)
                if cat:
                    result['category'] = cat
            break
    else:
        result['intent'] = 'unknown'
    # Time range extraction
    time_range = parse_time_range(query)
    result['time_range'] = time_range
    return result

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:])
    else:
        query = input('Enter your query: ')
    parsed = parse_intent_and_entities(query)
    print(json.dumps(parsed, indent=2)) 