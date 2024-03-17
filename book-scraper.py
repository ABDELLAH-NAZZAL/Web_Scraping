import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL for the website to scrape
BASE_URL = "https://books.toscrape.com/catalogue/" 

def scrape_books_data(num_pages):
    """Scrapes book information from the specified number of pages.

    Args:
        num_pages (int): The number of pages to scrape.

    Returns:
        list: A list of dictionaries, where each dictionary represents a book.
    """

    books = []
    for page_num in range(1, num_pages + 1):
        page_url = f"{BASE_URL}page-{page_num}.html"
        response = requests.get(page_url)
        response.raise_for_status()  # Check for errors

        soup = BeautifulSoup(response.content, 'html.parser')
        book_articles = soup.find_all('article', class_='product_pod')

        for article in book_articles:
            title = article.find('img')['alt']
            star_rating = article.find('p')['class'][1]
            price_str = article.find('p', class_='price_color').text.strip('£')
            price = float(price_str)

            books.append({
                'Title': title,
                'Price': price,
                'Star Rating': star_rating
            })

    return books

if __name__ == '__main__':
    num_pages = 50  # Number of pages to scrape
    books_data = scrape_books_data(num_pages)

    df = pd.DataFrame(books_data)
    df.to_csv("books.csv")  # Change the output file path as needed
