# Installation Guide

## Using Pipenv

1. Install Pipenv (if not already installed):
   ```
   pip install pipenv
   ```
2. Install project dependencies:
   ```
   pipenv install
   ```
3. Create a `.env` file from the example:
   ```
   cp .env.example .env
   ```
4. Activate the Pipenv virtual environment:
   ```
   pipenv shell
   ```
5. Run the application:
   ```
   python app.py
   ```

## Using Docker Compose

1. Build and start the Docker containers:
   ```
   docker compose -f docker-compose-dev.yaml up
   ```
2. The application will be accessible at `http://127.0.0.1:5000`.

# Usage

## API Usage

Request:

```
GET http://127.0.0.1:5000/scrape?title=godfather
```

Response:

```
{
    "title": "The Godfather",
    "year": "1972",
    "url": "https://www.imdb.com/title/tt0068646/",
    "actors": "Marlon Brando, Al Pacino",
    "poster_url": "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_QL75_UY74_CR1,0,50,74_.jpg",
    "imdbID": "tt0068646",
    "plot_summary": "Don Vito Corleone, head of a mafia family, decides to hand over his empire to his youngest son, Michael. However, his decision unintentionally puts the lives of his loved ones in grave danger.",
    "awards": "Won 3 Oscars",
    "awards_total": "31 wins & 31 nominations total",
    "directors": [
        "Francis Ford Coppola"
    ],
    "rating": "9.2",
    "runtime": "2h 55m",
    "age_restriction": "R"
}
```

## Using params in Postman:

Request:

- Method: GET
- URL: http://127.0.0.1:5000/scrape
- Params:
  - Key: title
  - Value: godfather

Response:

```
{
    "title": "The Godfather",
    "year": "1972",
    "url": "https://www.imdb.com/title/tt0068646/",
    "actors": "Marlon Brando, Al Pacino",
    "poster_url": "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_QL75_UY74_CR1,0,50,74_.jpg",
    "imdbID": "tt0068646",
    "plot_summary": "Don Vito Corleone, head of a mafia family, decides to hand over his empire to his youngest son, Michael. However, his decision unintentionally puts the lives of his loved ones in grave danger.",
    "awards": "Won 3 Oscars",
    "awards_total": "31 wins & 31 nominations total",
    "directors": [
        "Francis Ford Coppola"
    ],
    "rating": "9.2",
    "runtime": "2h 55m",
    "age_restriction": "R"
}
```
