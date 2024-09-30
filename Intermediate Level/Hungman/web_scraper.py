
import json
from bs4 import BeautifulSoup
import requests
def fetch_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page content: {e}")
        return None
def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
# URL to scrape
url = "https://www.shadowfox.in/#"
# Fetching the HTML content using requests
page_content = fetch_page_content(url)
if page_content:
    soup = BeautifulSoup(page_content, 'html.parser')
    title = soup.find('title')
    qwery = soup.find('h1')
    links = soup.find('a')
    many_link = soup.find_all('a')
    total_links = len(many_link)
    second_link = many_link[1] if len(many_link) > 1 else None
    nested_div = second_link.find('div') if second_link else None
    z = nested_div['class'] if nested_div and 'class' in nested_div.attrs else []
    data_to_save = {
        "title": title.text if title else "No title found",
        "h1": qwery.text if qwery else "No h1 tag found",
        "links": [a['href'] for a in soup.find_all('a', href=True)],
        "total_links": total_links,
        "second_link": {
            "html": str(second_link),
            "href": second_link['href'] if second_link and 'href' in second_link.attrs else "No href found"
        } if second_link else "No second link found"
    }
    # Save to JSON file
    save_to_json(data_to_save, 'output.json')
else:
    print("Failed to fetch the page content.")