"""Django settings for local environment."""

import os

from {{project_name}}.settings.base import *  # noqa


# Security
# https://docs.djangoproject.com/en/2.2/topics/security/#host-header-validation

BASE_URL = '{{project_name}}.local'

BASE_DOMAIN_URL = f'http://{BASE_URL}'

ALLOWED_HOSTS = (BASE_URL, '127.0.0.1', 'localhost')


# Debug

DEBUG = True


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

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Django CORS Headers
# https://github.com/ottoyiu/django-cors-headers/

CORS_ORIGIN_ALLOW_ALL = True


# Debug Toolbar

try:
    import debug_toolbar  # noqa
except ModuleNotFoundError:
    pass
else:
    INTERNAL_IPS = ['127.0.0.1', 'localhost']
    INSTALLED_APPS.append('debug_toolbar')  # noqa
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')  # noqa
