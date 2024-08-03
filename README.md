## API Usage:

Request:
```
GET http://127.0.0.1:5000/scrape?title=godfather
```
Response:
```
{
  "title": "The Godfather",
  "url": "https://www.imdb.com/title/tt0068646/",
  "year": "1972"
}
```
## Using params in Postman:

Request:

* Method: GET
* URL: http://127.0.0.1:5000/scrape
* Params:
    * Key: title
    * Value: godfather 

Response:
```
{
  "title": "The Godfather",
  "url": "https://www.imdb.com/title/tt0068646/",
  "year": "1972"
}
```
