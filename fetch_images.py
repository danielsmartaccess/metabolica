import requests
from bs4 import BeautifulSoup
import re

def get_images(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        images = []
        for img in soup.find_all('img'):
            src = img.get('src')
            if src and src.startswith('http'):
                images.append(src)
        return images
    except Exception as e:
        return [str(e)]

url = "https://www.crossfit.com/190405?topicId=cfdailyfc.20190405"
print(f"Images for {url}:")
for img in get_images(url):
    print(img)
