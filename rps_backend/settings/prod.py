"""
Production specific settings for your app (Heroku settings)
"""
import os
from .base import *

import django_heroku

# We dont want Django debug messages showing up in production
# | this can expose your underlying system to the public.
# | but if for some reason we needed them we can set Heroku Config var.
DEBUG = os.environ.get('DEBUG', 0)


SECRET_KEY = os.environ.get('SECRET_KEY') # Lets Django read Heroku Config Vars

# Heroku Config Var would store:
# | ALLOWED_HOST : chrisrh-rps-api.herokuapp.com
# | Django reads it in: 'chrisrh-rps-api.herokuapp.com'.split()
# | produces this ['chrisrh-rps-api.herokuapp.com']
# | otherwise if Config Var is missing its ''.split() -> []
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split()

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'rest_framework',
    'accounts', 
    'rpsgame',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'], # raise KeyError if missing.
    }
}

# REST FRAMEWORK SETTINGS
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    # We are only accepting JSON Web Tokens (JWT Tokens)
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',
        'user': '1000/hour'
    }
}


JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'accounts.utils.my_jwt_response_handler',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=3600), # 1 hour
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', '').split()
allow_all_origins = True if os.environ.get('CORS_ALLOW_ALL_ORIGINS', 0) else False
CORS_ALLOW_ALL_ORIGINS = os.environ.get('CORS_ALLOW_ALL_ORIGINS', allow_all_origins)
django_heroku.settings(locals())
