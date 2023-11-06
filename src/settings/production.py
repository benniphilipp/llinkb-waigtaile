import os
from pathlib import Path
import urllib3
import environ

from .base import *


env = environ.Env(
    ENVIRONMENT=(str, "local"),
    DEBUG=(bool, False)
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
env = os.environ.copy()

DEBUG = False

SECRET_KEY = env['SECRET_KEY']
ALLOWED_HOSTS=['llinkb.be', 'www.llinkb.be']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wagtail',
        'USER': 'wagtail_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}


CORS_ORIGIN_ALLOW_ALL = True   
SECURE_SSL_REDIRECT = True
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

try:
    from .local import *
except ImportError:
    pass
