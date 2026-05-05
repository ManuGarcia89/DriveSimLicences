import os
from .base import *

DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-prod-key-123')

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
    'https://api.jausim.com',
    'http://api.jausim.com',
    'https://*.jausim.com'
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'drivesim_db'),
        'USER': os.environ.get('POSTGRES_USER', 'drivesim_user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'drivesim_pass'),
        'HOST': os.environ.get('DB_HOST', 'db'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}
