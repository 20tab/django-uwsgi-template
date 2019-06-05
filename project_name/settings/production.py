"""Django settings for production environment."""

import os

from {{project_name}}.settings.base import *  # noqa


# Security
# https://docs.djangoproject.com/en/2.2/topics/security/#host-header-validation

ALLOWED_HOSTS = (BASE_URL,)  # noqa


# Debug

DEBUG = False


# Database
# https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_DEFAULT_NAME', '{{project_name}}'),
        'USER': os.getenv('DATABASE_DEFAULT_USER', '{{project_name}}'),
        'PASSWORD': os.getenv('DATABASE_DEFAULT_PASSWORD', ''),
        'HOST': os.getenv('DATABASE_DEFAULT_HOST', '127.0.0.1'),
        'PORT': os.getenv('DATABASE_DEFAULT_PORT', '5432'),
    }
}


# Deployment
# https://docs.djangoproject.com/en/{{docs_version}}/howto/deployment/checklist/

SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = 'DENY'  # Default: 'SAMEORIGIN'

# CSRF_COOKIE_SECURE = True

# SECURE_SSL_REDIRECT = True

# SESSION_COOKIE_SECURE = True

# CONN_MAX_AGE = None
