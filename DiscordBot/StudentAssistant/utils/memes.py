import requests

def get_meme():
    response = requests.get("https://meme-api.com/gimme")
    if response.status_code == 200:
        data = response.json()
        return data['url']
    return "Failed to fetch meme."

# student_bot/utils/quotes.py
import requests

def get_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        return f'"{data["content"]}" — {data["author"]}'
    return "Couldn't fetch a quote at this time."
