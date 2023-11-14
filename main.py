from bs4 import BeautifulSoup
import requests
import re

# URL halaman yang akan di scrape
url = 'https://www.pikiran-rakyat.com/'

# Set up user agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Fetch konten HTML
response = requests.get(url, headers=headers)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

# Mencari section article populer
section = soup.find('section', class_='most mt2 clearfix')

# Inisialisasi list untuk menyimpan judul dan url artikel
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

        # Mengambil konten HTML artikel
        response = requests.get(paginated_url, headers=headers)
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

    return article_content.strip()

def sanitize_filename(filename):
    # Membersihkan karakter ilegal untuk nama file
    return re.sub(r'[\\/*?:"<>|]', '', filename)

total_fetched = 0

# Looping untuk menyimpan konten setiap artikel ke file .txt
for i in range(len(urls)):
    article_text = scrape_article_content(urls[i])
    safe_title = sanitize_filename(titles[i])
    file_path = f'articles/{safe_title}.txt'
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(article_text)
        print("Total articles fetched: " + str(total_fetched + 1 + i) + "\n")   