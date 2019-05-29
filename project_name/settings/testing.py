"""Django settings for testing environment."""

from {{project_name}}.settings.base import *  # noqa
from {{project_name}}.settings.secret import *  # noqa

HOST = BASE_HOST_URL  # noqa

ALLOWED_HOSTS = (HOST,)


# Database
# https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DATABASES_DEFAULT_NAME or '{{project_name}}_test',  # noqa
        'USER': DATABASES_DEFAULT_USER or '{{project_name}}',  # noqa
        'PASSWORD': DATABASES_DEFAULT_PASSWORD or '',  # noqa
        'HOST': DATABASES_DEFAULT_HOST or '127.0.0.1',  # noqa
        'PORT': DATABASES_DEFAULT_PORT or '5432',  # noqa
    }
}


# Email Settings
# https://docs.djangoproject.com/en/{{docs_version}}/topics/email/

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'


# Debug

DEBUG = False

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # noqa


# Django REST Framework
# https://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {}
