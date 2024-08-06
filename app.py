from flask import Flask, request, Response, jsonify
import requests
from bs4 import BeautifulSoup
import time
from collections import OrderedDict
import json

app = Flask(__name__)

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
                href = result['href']
                imdb_id = href.split('/')[2]

                first_result_url = f"https://www.imdb.com{href.split('?')[0]}"
                first_result_title = result.text.strip()

                # Extract the year
                year_ul = result.find_next('ul', class_='ipc-inline-list')
                year_span = year_ul.find('span', class_='ipc-metadata-list-summary-item__li')
                first_result_year = year_span.text.strip() if year_span else "N/A"

                # Extract the actors
                actors_ul = year_ul.find_next('ul', class_='ipc-inline-list')
                actors_span = actors_ul.find('span', class_='ipc-metadata-list-summary-item__li')
                actors = actors_span.text.strip() if actors_span else "N/A"

                poster_img = soup.find('img', class_='ipc-image')
                first_result_poster_url = poster_img['src'] if poster_img else None

                # Additional data extraction from the movie's detailed page
                try:
                    detail_response = requests.get(first_result_url, headers=headers)
                    detail_response.raise_for_status()
                    detail_soup = BeautifulSoup(detail_response.text, 'html.parser')

                    # Extract plot summary
                    plot_summary = detail_soup.find('span', {'data-testid': 'plot-xl'}).text.strip() if detail_soup.find('span', {'data-testid': 'plot-xl'}) else "N/A"

                    # Extract awards
                    award_info = detail_soup.find('li', {'data-testid': 'award_information'})
                    if award_info:
                        award_text = award_info.find('a', class_='ipc-metadata-list-item__label')
                        awards_text = award_text.text.strip() if award_text else "None"

                        awards_details = award_info.find('span', class_='ipc-metadata-list-item__list-content-item')
                        awards_total = awards_details.text.strip() if awards_details else "None"
                    else:
                        awards_text = "None"
                        awards_total = "None"

                    # Extract directors
                    directors_list = detail_soup.find('ul', class_='ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content baseAlt')
                    if directors_list:
                        director_tags = directors_list.find_all('a', class_='ipc-metadata-list-item__list-content-item')
                        directors = [tag.text.strip() for tag in director_tags]
                    else:
                        directors = []

                    # Extract rating
                    rating_div = detail_soup.find('div', {'data-testid': 'hero-rating-bar__aggregate-rating__score'})
                    rating = rating_div.find('span', class_='sc-eb51e184-1 ljxVSS').text.strip() if rating_div else "N/A"

                    result_data = OrderedDict([
                        ('title', first_result_title),
                        ('year', first_result_year),
                        ('url', first_result_url),
                        ('actors', actors),
                        ('poster_url', first_result_poster_url),
                        ('imdbID', imdb_id),
                        ('plot_summary', plot_summary),
                        ('awards', awards_text),
                        ('awards_total', awards_total),
                        ('directors', directors),
                        ('rating', rating)
                    ])

                    return result_data
                except requests.RequestException as e:
                    print(f"Error fetching movie details: {e}")

            else:
                return None

        except requests.RequestException as e:
            print(f"Attempt {i + 1} - Error fetching search results: {e}")
            time.sleep(2)

    return None

@app.route('/scrape', methods=['GET'])
def scrape():
    movie_title = request.args.get('title')
    if not movie_title:
        return jsonify({'error': 'No movie title provided'}), 400

    result = scrape_imdb(movie_title)
    if result:
        response = Response(json.dumps(result), mimetype='application/json')
        return response
    else:
        return jsonify({'error': 'No results found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
