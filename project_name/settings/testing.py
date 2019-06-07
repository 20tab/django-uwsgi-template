"""Django settings for testing environment."""

import os

from {{project_name}}.settings.base import *  # noqa


# Security
# https://docs.djangoproject.com/en/{{docs_version}}/topics/security/#host-header-validation

ALLOWED_HOSTS = (BASE_URL,)  # noqa


# Debug
# https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#debug

DEBUG = False


# Database
# https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASES_DEFAULT_NAME', '{{project_name}}'),
        'USER': os.getenv('DATABASES_DEFAULT_USER', '{{project_name}}'),
        'PASSWORD': os.getenv('DATABASES_DEFAULT_PASSWORD', ''),
        'HOST': os.getenv('DATABASES_DEFAULT_HOST', '127.0.0.1'),
        'PORT': os.getenv('DATABASES_DEFAULT_PORT', '5432'),
    }
}


# Email Settings
# https://docs.djangoproject.com/en/{{docs_version}}/topics/email/

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'


# Django REST Framework
# https://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {}
