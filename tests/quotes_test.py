from api_test.quotes import get_quotes
from api_test.common import save_json, to_json
# pip install -e . 


quotes = get_quotes()
quote = quotes[0]
print(f"{quote['text']} - {quote['author']}")

json_str = to_json(quotes)

location = './tests/quotes.json'
save_json(json_str=json_str, location=location)