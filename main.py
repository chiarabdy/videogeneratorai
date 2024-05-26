import requests

def fetch_quotes():
    url = 'https://stoic-quotes.com/api/quote'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Example usage
quote = fetch_quotes()
if quote:
    print(f"Quote: {quote['text']} - {quote['author']}")
