import os
from environ import Env

env = Env()
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
