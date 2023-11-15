from bs4 import BeautifulSoup
import requests
import re
import json

# URL halaman yang akan di scrape
url = 'https://www.pikiran-rakyat.com/'

# Set up user agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

# Fetch konten HTML
response = requests.get(url, headers=headers)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

# Mencari section article populer
section = soup.find('section', class_='most mt2 clearfix')

# Inisialisasi list untuk menyimpan judul dan url artikel
articles = {}
titles =[]
urls = []

if section:
    # Mencari semua elemen 'h2' dengan class 'most__title' dan parent 'a' tag
    print("Fetching the article title and URLs...\n")
    links = section.find_all('a', class_='most__link')

    # Extract dan print judul artikel
    for link in links:
        title = link.find('h2', class_='most__title')
        if title:
            print("Article found, title: " + title.text)
            titles.append(title.text)
            urls.append(link['href'])
else:
    print("Section with the specified class not found.")

def scrape_article_content(article_url):
    article_content = ""
    page_number = 1  # Mulai dari halaman pertama
    while True:
        # Check apakah di halaman pertama
        if page_number > 1:
            paginated_url = f"{article_url}?page={page_number}"
        else:
            paginated_url = article_url

        try:
            # Mengambil konten HTML artikel
            response = requests.get(paginated_url, headers=headers, timeout=10)
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')

            # Mencari elemen konten artikel
            article_body = soup.find('article', class_='read__content clearfix')

            if article_body:
                for p in article_body.find_all('p'):
                    # Menskip paragraf yang berisi link ke artikel lain
                    if 'Baca Juga:' not in p.text and not p.find('a'):
                        article_content += p.text + "\n\n"

            # Mencari link 'Next' untuk halaman berikutnya
            next_page_link = soup.find('a', class_='paging__link', rel='next')

            if next_page_link:
                page_number += 1
            else:
                break
        except requests.exceptions.RequestException as e:
            print(f"Error fetching response. Error: {e}")
            break

    return article_content.strip()

# Export ke articles.json dengan struktur {title:{konten:link}}

for i in range(len(titles)):
    articles[titles[i]] = {
        "content": scrape_article_content(urls[i]),
        "link": urls[i]
    }

with open('articles.json', 'w') as outfile:
    json.dump(articles, outfile, indent=4)
    print("Done writing to articles.json")
