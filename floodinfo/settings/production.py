from .base import *
import dj_database_url

DEGUB = False

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
DATABASES['default'] =  dj_database_url.config()
ALLOWED_HOSTS = ['*']
