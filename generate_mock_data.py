import csv
import random
from datetime import datetime, timedelta

CATEGORIES = [
    'food', 'entertainment', 'transport', 'shopping', 'bills', 'health', 'salary', 'investment', 'gift', 'other'
]
CATEGORY_TYPE = {
    'food': 'expense',
    'entertainment': 'expense',
    'transport': 'expense',
    'shopping': 'expense',
    'bills': 'expense',
    'health': 'expense',
    'salary': 'income',
    'investment': 'income',
    'gift': 'income',
    'other': random.choice(['income', 'expense'])
}

DESCRIPTIONS = {
    'food': ['restaurant', 'groceries', 'cafe', 'snacks'],
    'entertainment': ['movie', 'concert', 'games', 'subscription'],
    'transport': ['bus', 'taxi', 'fuel', 'train'],
    'shopping': ['clothes', 'electronics', 'online shopping'],
    'bills': ['electricity', 'water', 'internet', 'rent'],
    'health': ['pharmacy', 'doctor', 'gym'],
    'salary': ['monthly salary', 'bonus'],
    'investment': ['stock dividend', 'crypto gain'],
    'gift': ['birthday gift', 'wedding gift'],
    'other': ['miscellaneous']
}

START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2024, 6, 1)
NUM_RECORDS = 1000

rows = []
for _ in range(NUM_RECORDS):
    days_offset = random.randint(0, (END_DATE - START_DATE).days)
    date = START_DATE + timedelta(days=days_offset)
    category = random.choice(CATEGORIES)
    type_ = CATEGORY_TYPE[category] if category != 'other' else random.choice(['income', 'expense'])
    if type_ == 'income':
        amount = round(random.uniform(1000, 5000), 2)
    else:
        amount = round(random.uniform(10, 500), 2)
    description = random.choice(DESCRIPTIONS[category])
    rows.append({
        'date': date.strftime('%Y-%m-%d'),
        'amount': amount,
        'category': category,
        'type': type_,
        'description': description
    })

with open('mock_transactions.csv', 'w', newline='') as csvfile:
    fieldnames = ['date', 'amount', 'category', 'type', 'description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

print(f"Generated {NUM_RECORDS} mock transactions in 'mock_transactions.csv'.") 