"""
This is an optional file that defined app level settings such as:
- database settings
- session settings
- i18n settings
This file is provided as an example:
"""
import os
# db settings
APP_FOLDER = os.path.dirname(__file__)
DB_FOLDER = os.path.join(APP_FOLDER, 'databases')
DB_URI = 'sqlite://storage.db'
DB_POOL_SIZE = 1

# session settings
SESSION_TYPE = 'cookies'
SESSION_SECRET_KEY = '<my secret key>'
MEMCACHE_CLIENTS = ['127.0.0.1:11211']
REDIS_SERVER = 'localhost:6379'

# single sign on Google (will be used if provided)
OAUTH2GOOGLE_CLIENT_ID = ''
OAUTH2GOOGLE_CLIENT_SECRET = ''


# single sign on Facebook (will be used if provided)
OAUTH2FACEBOOK_CLIENT_ID = ''
OAUTH2FACEBOOK_CLIENT_SECRET = ''

# i18n settings
T_FOLDER = os.path.join(APP_FOLDER, 'translations')
