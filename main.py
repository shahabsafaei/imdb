import requests
from bs4 import BeautifulSoup
import time

def scrape_imdb(movie_title):
    search_url = f"https://www.imdb.com/find?q={movie_title.replace(' ', '+')}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.0) Gecko/20100101 Firefox/128.0'
    }
    retries = 3

    for i in range(retries):
        try:
            response = requests.get(search_url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            result = soup.find('a', class_='ipc-metadata-list-summary-item__t')
            if result:
                first_result_url = f"https://www.imdb.com{result['href']}"
                first_result_url = first_result_url.split('?')[0]
                first_result_title = result.text.strip()

                year_span = result.find_next('span', class_='ipc-metadata-list-summary-item__li')
                first_result_year = year_span.text.strip() if year_span else "N/A"

                return {
                    'title': first_result_title,
                    'year': first_result_year,
                    'url': first_result_url
                }
            else:
                print("No results found.")
                return None

        except requests.RequestException as e:
            print(f"Attempt {i + 1} - Error fetching data: {e}")
            time.sleep(2)

    print("Failed to fetch data after multiple attempts.")
    return None

movie_title = input("Enter the movie title: ")
result = scrape_imdb(movie_title)
if result:
    print(f"Movie Title: {result['title']}")
    print(f"Year: {result['year']}")
    print(f"URL: {result['url']}")
else:
    print("No results found.")
