from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-vksuz$!6vb)cyglv*(7mijr44d0x(%5#7xs7d@7n9zs=!s0re3"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["localhost", "89.58.32.21:8000", "*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
CSRF_TRUSTED_ORIGINS = ["https://*.llinkb.be"]

try:
    from .local import *
except ImportError:
    pass
