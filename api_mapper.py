from urllib.parse import urlencode

def map_to_api(parsed: dict) -> str:
    intent = parsed.get('intent')
    category = parsed.get('category')
    time_range = parsed.get('time_range')
    base_url = '/report/'
    params = {}

    if intent == 'category_expense' and category and time_range:
        base_url += 'by-category'
        params['category'] = category
        params['start'] = time_range['start']
        params['end'] = time_range['end']
    elif intent == 'income_vs_expense' and time_range:
        base_url += 'income-vs-expense'
        params['start'] = time_range['start']
        params['end'] = time_range['end']
    elif intent == 'top_category' and time_range:
        base_url += 'top-category'
        params['start'] = time_range['start']
        params['end'] = time_range['end']
    elif intent == 'daily_expenses' and time_range:
        base_url += 'daily-expenses'
        params['start'] = time_range['start']
        params['end'] = time_range['end']
    elif intent == 'income' and time_range:
        base_url += 'income'
        params['start'] = time_range['start']
        params['end'] = time_range['end']
    elif intent == 'expense' and time_range:
        base_url += 'expense'
        params['start'] = time_range['start']
        params['end'] = time_range['end']
    else:
        base_url += 'unknown'
    if params:
        return f"{base_url}?{urlencode(params)}"
    else:
        return base_url

if __name__ == '__main__':
    import json
    sample = {
        "intent": "category_expense",
        "category": "food",
        "time_range": {"start": "2024-05-01", "end": "2024-05-31"}
    }
    print(map_to_api(sample)) 