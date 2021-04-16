"""
Production specific settings for your app (Heroku settings)
"""
import os
from .base import *

import django_heroku

# We dont want Django debug messages showing up in production
# | this can expose your underlying system to the public.
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
# TODO: We will change this when we deploy.
# | '<heroku app url>' goes in place of '*'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split()

MIDDLEWARE = [
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

django_heroku.settings(locals())
