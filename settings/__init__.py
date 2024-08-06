"""
Initializes the app settings based on the current environment mode.
"""

import os

from .base import *

MODE = os.environ.get('APP_ENV_MODE', 'DEV')

if MODE == 'PROD':
    from .production import *
elif MODE == 'DEV':
    from .development import *
