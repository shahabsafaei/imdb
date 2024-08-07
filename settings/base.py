"""
Initializes the app base settings.
These settings are common between production and development environments.
"""

import os

BASE_URL = "https://www.imdb.com"

REQUEST_HEADERS = {
    'User-Agent': os.environ.get('APP_REQUEST_USER_AGENT', 'imdbAPI/1.0')
}

REQUEST_TIMEOUT = 30

MAX_RETRIES = 3
