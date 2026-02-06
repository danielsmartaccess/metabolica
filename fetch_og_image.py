import requests
from bs4 import BeautifulSoup

def get_og_image(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        og_image = soup.find("meta", property="og:image")
        if og_image:
            return og_image["content"]
        else:
            return "No og:image found"
    except Exception as e:
        return str(e)

print(get_og_image("https://www.crossfit.com/190405?topicId=cfdailyfc.20190405"))
