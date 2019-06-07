"""Django settings for beta environment."""

import os

from {{project_name}}.settings.base import *  # noqa


# Security
# https://docs.djangoproject.com/en/2.2/topics/security/#host-header-validation

BASE_URL = f'beta.{BASE_HOST_URL}'  # noqa

BASE_DOMAIN_URL = f'http://{BASE_URL}'

ALLOWED_HOSTS = (BASE_URL,)


# Debug

DEBUG = False


# Database
# https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASES_DEFAULT_NAME', '{{project_name}}_beta'),
        'USER': os.getenv('DATABASES_DEFAULT_USER', '{{project_name}}'),
        'PASSWORD': os.getenv('DATABASES_DEFAULT_PASSWORD', ''),
        'HOST': os.getenv('DATABASES_DEFAULT_HOST', '127.0.0.1'),
        'PORT': os.getenv('DATABASES_DEFAULT_PORT', '5432'),
    }
}
