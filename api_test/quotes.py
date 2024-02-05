import requests

def get_quotes():
    url = "https://type.fit/api/quotes"
    response = requests.get(url)    
    quotes = []
    if response.status_code == 200:
        quotes = response.json()                 
    else:
        print("Failed to retrieve quotes")
    return quotes