from __future__ import absolute_import, unicode_literals
import os
from .base import *

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



try:
    from .local import *
except ImportError:
    pass
