from rapidfuzz import process, fuzz

CATEGORIES = [
    'food', 'entertainment', 'transport', 'shopping', 'bills', 'health', 'salary', 'investment', 'gift', 'other'
]

SYNONYMS = {
    'restaurant': 'food',
    'groceries': 'food',
    'cafe': 'food',
    'snacks': 'food',
    'movie': 'entertainment',
    'concert': 'entertainment',
    'games': 'entertainment',
    'subscription': 'entertainment',
    'bus': 'transport',
    'taxi': 'transport',
    'fuel': 'transport',
    'train': 'transport',
    'clothes': 'shopping',
    'electronics': 'shopping',
    'online shopping': 'shopping',
    'electricity': 'bills',
    'water': 'bills',
    'internet': 'bills',
    'rent': 'bills',
    'pharmacy': 'health',
    'doctor': 'health',
    'gym': 'health',
    'salary': 'salary',
    'bonus': 'salary',
    'stock dividend': 'investment',
    'crypto gain': 'investment',
    'birthday gift': 'gift',
    'wedding gift': 'gift',
    'miscellaneous': 'other',
    'restraunt': 'food',  # common typo
    'resturant': 'food',  # another typo
    'medicines': 'health',
    'medicine': 'health',
    'doctor visit': 'health',
}

FUZZY_THRESHOLD = 80

def resolve_category(text: str) -> str:
    text = text.lower().strip()
    # Check synonyms first
    if text in SYNONYMS:
        return SYNONYMS[text]
    # Fuzzy match against categories
    match, score, _ = process.extractOne(text, CATEGORIES, scorer=fuzz.ratio)
    if score >= FUZZY_THRESHOLD:
        return match
    # Fuzzy match against synonyms
    syn_match, syn_score, _ = process.extractOne(text, list(SYNONYMS.keys()), scorer=fuzz.ratio)
    if syn_score >= FUZZY_THRESHOLD:
        return SYNONYMS[syn_match]
    return None

if __name__ == '__main__':
    tests = ['restraunt', 'groceries', 'medicines', 'entertainmnt', 'bus', 'cloths', 'doctor visit']
    for t in tests:
        print(f'{t} -> {resolve_category(t)}') 