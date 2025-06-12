# WalletSync NLP Demo

This project demonstrates a robust natural language query parser for user financial queries in the WalletSync app. It extracts intent, category, and time range from user queries and maps them to API endpoints, even when queries contain typos or synonyms.

---

## Features
- **Intent and entity extraction** from user queries
- **Robust time range parsing** (e.g., "last month", "April 2024", "in May")
- **Fuzzy matching and synonym handling** for categories (e.g., "restraunt" → "food")
- **Spell correction** for user queries (e.g., "spemd" → "spend")
- **Fuzzy and semantic intent detection** for typo-tolerant intent recognition
- **CLI demo** for interactive testing
- **Synthetic data generator** for mock transactions
- **Unit tests** for all core modules
- **Flexible API mapping**: API URLs are generated even if time range or category is missing, returning the most specific URL possible

---

## Technologies Used
- **Python 3.7+**
- [dateparser](https://dateparser.readthedocs.io/) – Natural language date parsing
- [rapidfuzz](https://maxbachmann.github.io/RapidFuzz/) – Fast fuzzy string matching
- [pyspellchecker](https://pyspellchecker.readthedocs.io/) – Spell correction
- [textblob](https://textblob.readthedocs.io/) – Advanced spell correction
- [sentence-transformers](https://www.sbert.net/) – Semantic intent detection
- [pytest](https://docs.pytest.org/) – Unit testing

---

## How the System Works (Pipeline Overview)
1. **Spell Correction:** User query is auto-corrected for common typos.
2. **Intent & Entity Parsing:** The system extracts intent, category, and time range using regex, fuzzy matching, and synonym mapping.
3. **Time Range Parsing:** Handles natural language time expressions, including single months, ranges, and relative dates.
4. **API Mapping:** The parsed output is mapped to a mock WalletSync API URL. If time or category is missing, the system returns the most specific URL possible (e.g., `/report/by-category?category=food`).
5. **CLI Demo:** Lets you interactively test the system with your own queries.

---

## Setup

1. **Clone or download this repository.**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Generate mock data (optional):**
   ```bash
   python generate_mock_data.py
   ```
4. **Download TextBlob corpora (required for spell correction):**
   ```bash
   python -m textblob.download_corpora
   ```

---

## Usage

### Run the CLI Demo
```bash
python walletsync_cli.py
```
- Enter your financial query (e.g., `How much did I spend on food last month?`).
- The CLI will show the parsed output and the mapped API URL.
- Type `exit` to quit.

#### Example Queries (with and without typos)
- What was my income vs expense last month?
- Which category had the highest spending in May?
- How much did I spend on entertainment this week?
- Show daily expenses for the last 7 days.
- How much did I spend on restraunt in April 2024?
- how much i spemd in last monthe
- show expens on food in may
- how much i spent on restaurnats
- how much i spent on food

**Example output for a query with only a category:**
```
Enter your query: how much i spent on restaurnats

Parsed Output:
{
  "intent": "category_expense",
  "category": "food",
  "time_range": null
}

API URL:
/report/by-category?category=food
```

---

## Running Unit Tests

To run all tests:
```bash
pytest
```

---

## File Overview
- `generate_mock_data.py` – Generates mock financial transactions (CSV)
- `walletsync/` – Core package with all logic:
  - `nlp_parser.py` – Main intent/entity parser (with spell correction & fuzzy/semantic intent)
  - `time_parser.py` – Time range parser
  - `fuzzy_category.py` – Fuzzy matching and synonym mapping for categories
  - `api_mapper.py` – Maps parsed output to API URLs
- `walletsync_cli.py` – CLI demo
- `tests/` – Unit tests for all modules

---

## Extending the System
- Add new intents or categories by updating the relevant lists and patterns in `walletsync/nlp_parser.py` and `walletsync/fuzzy_category.py`.
- Improve time parsing by extending `walletsync/time_parser.py`.
- Integrate with real APIs by replacing the mock API mapping logic.

---

## License
MIT 