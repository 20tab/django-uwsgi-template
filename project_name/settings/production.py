"""Django settings for production environment."""

from {{project_name}}.settings.base import *  # noqa
from {{project_name}}.settings.secret import *  # noqa


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
        'NAME': DATABASES_DEFAULT_NAME or '{{project_name}}',  # noqa
        'USER': DATABASES_DEFAULT_USER or '{{project_name}}',  # noqa
        'PASSWORD': DATABASES_DEFAULT_PASSWORD or '',  # noqa
        'HOST': DATABASES_DEFAULT_HOST or '127.0.0.1',  # noqa
        'PORT': DATABASES_DEFAULT_PORT or '5432',  # noqa
    }
}


# Email Settings
# https://docs.djangoproject.com/en/{{docs_version}}/topics/email/

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = EMAIL_HOST or ''  # noqa


# Deployment
# https://docs.djangoproject.com/en/{{docs_version}}/howto/deployment/checklist/

SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = 'DENY'  # Default: 'SAMEORIGIN'

# CSRF_COOKIE_SECURE = True

# SECURE_SSL_REDIRECT = True

# SESSION_COOKIE_SECURE = True

# CONN_MAX_AGE = None
