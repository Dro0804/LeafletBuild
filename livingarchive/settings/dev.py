from .base import *
import os 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bmxu&vi39=^=a^1zto6u5t(1dr1f5a^47_of!+m%p6ar*w5a^v'
MIRAGE_SECRET_KEY = 'gdhhgi%&HGKJ*F___fdffhdjfhsh===%@ghg'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*','localhost'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
WAGTAILADMIN_BASE_URL="http://localhost:8002"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'bhagwatithakuri77@gmail.com'
EMAIL_HOST_PASSWORD = 'tjyp zofa pfaw vmmc'
DEFAULT_FROM_EMAIL ="Living Archive <bhagwatithakuri77@gmail.com>"

try:
    from .local import *
except ImportError:
    pass
