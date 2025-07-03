import requests

def get_quote(tag=None):
    url = "https://api.quotable.io/random"
    if tag:
        url += f"?tags={tag}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f'🧠 \"{data["content"]}\" — *{data["author"]}*'
        elif response.status_code == 404:
            return "❌ No quotes found for this tag."
        else:
            return "⚠️ Couldn't fetch a quote right now."
    except Exception as e:
        return f"⚠️ Error: {e}"


# Optional: Validate tag if needed
def is_valid_tag(tag):
    valid_tags = ["famous-quotes", "technology", "wisdom", "inspirational", "friendship", "life", "success"]
    return tag in valid_tags
