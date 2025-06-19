import requests
from bs4 import BeautifulSoup

# Step 1: Add headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

url = "https://www.hindustantimes.com/"

# Step 2: Send GET request with headers
response = requests.get(url, headers=headers)

# Step 3: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Find all headlines
headlines = soup.find_all(['h1', 'h2', 'h3'])

print("📰 Top Headlines:\n")
for idx, headline in enumerate(headlines[:10], 1):
    text = headline.get_text(strip=True)
    if text and "Access Denied" not in text:
        print(f"{idx}. {text}")





