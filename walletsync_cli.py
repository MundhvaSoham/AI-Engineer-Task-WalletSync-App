"""
CLI demo for WalletSync NLP query parser.
Allows interactive testing of natural language queries.
"""
import json
from walletsync.nlp_parser import parse_intent_and_entities
from walletsync.api_mapper import map_to_api

def main() -> None:
    """
    Run the WalletSync CLI demo loop.
    """
    print("WalletSync Query Demo (type 'exit' to quit)")
    while True:
        query = input('\nEnter your query: ')
        if query.strip().lower() == 'exit':
            break
        parsed = parse_intent_and_entities(query)
        print("\nParsed Output:")
        print(json.dumps(parsed, indent=2))
        api_url = map_to_api(parsed)
        print("\nAPI URL:")
        print(api_url)

if __name__ == '__main__':
    main() 