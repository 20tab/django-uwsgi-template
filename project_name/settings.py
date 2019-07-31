"""
Django settings for {{project_name}} project.

Generated by 'django-admin startproject' using Django {{django_version}}.

For more information on this file, see
https://docs.djangoproject.com/en/{{docs_version}}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/
"""

import os
from typing import List

from configurations import Configuration, values


class DjangoDefault(Configuration):
    """
    The default settings from the Django project template.

    Django Configurations
    https://django-configurations.readthedocs.io
    """

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/{{docs_version}}/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = values.SecretValue()

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS: List[str] = []

    # Application definition

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "{{project_name}}.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ]
            },
        }
    ]

    WSGI_APPLICATION = "{{project_name}}.wsgi.application"

    # Database
    # https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#databases

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

    # Password validation
    # https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#auth-password-validators  # noqa
    # fmt: off
    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]
    # fmt: on
    # Internationalization
    # https://docs.djangoproject.com/en/{{docs_version}}/topics/i18n/

    LANGUAGE_CODE = "en-us"

    TIME_ZONE = "UTC"

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/{{docs_version}}/howto/static-files/

    STATIC_URL = "/static/"


class ProjectDefault(DjangoDefault):
    """The common settings."""

    # Application definition

    DjangoDefault.INSTALLED_APPS.extend(["rest_framework"])

    # Database URL
    # https://django-configurations.readthedocs.io/en/stable/values/

    DATABASES = values.DatabaseURLValue()

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/{{docs_version}}/howto/static-files/

    STATIC_ROOT = os.path.abspath(os.path.join(DjangoDefault.BASE_DIR, "static"))

    STATICFILES_STORAGE = (
        "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
    )

    # Stored files
    # https://docs.djangoproject.com/en/{{docs_version}}/topics/files/

    MEDIA_URL = "/media/"

    MEDIA_ROOT = os.path.abspath(os.path.join(DjangoDefault.BASE_DIR, "media"))

    # Site

    DEFAULT_NAME = "{{project_name}}"

    BASE_HOST_URL = "{{project_name}}.com"

    BASE_URL = f"www.{BASE_HOST_URL}"

    BASE_DOMAIN_URL = f"https://{BASE_URL}"

    # Email Settings
    # https://docs.djangoproject.com/en/{{docs_version}}/topics/email/

    SERVER_EMAIL = f"info@{BASE_HOST_URL}"

    DEFAULT_FROM_EMAIL = f"{DEFAULT_NAME} <{SERVER_EMAIL}>"

    EMAIL_SUBJECT_PREFIX = f"[{DEFAULT_NAME}] "

    ERROR_EMAIL = f"errors@{BASE_HOST_URL}"

    EMAIL_SIGNATURE = f"\n-- \n{DEFAULT_FROM_EMAIL}"

    MANAGERS = ((DEFAULT_NAME, ERROR_EMAIL),)

    ADMINS = MANAGERS

    EMAIL_USE_LOCALTIME = True

    # Translation
    # https://docs.djangoproject.com/en/{{docs_version}}/topics/i18n/translation/

    # LANGUAGES = (("en", "English"), ("it", "Italiano"))

    # LOCALE_PATHS = (os.path.abspath(os.path.join(DjangoDefault.BASE_DIR, "locale")),)

    # Authentication
    # https://docs.djangoproject.com/en/{{docs_version}}/topics/auth/customizing/

    # AUTH_USER_MODEL = "users.User"

    # LOGIN_URL = "login"

    # LOGOUT_URL = "logout"

    # LOGIN_ERROR_URL = "home"

    # LOGIN_REDIRECT_URL = "home"

    # LOGOUT_REDIRECT_URL = "home"

    # Django REST Framework
    # https://www.django-rest-framework.org/api-guide/settings/

    REST_FRAMEWORK = {}  # type: ignore


class Local(ProjectDefault):
    """The local settings."""

    # Security
    # https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#allowed-hosts

    BASE_URL = "{{project_name}}.local"

    BASE_DOMAIN_URL = f"http://{BASE_URL}"

    ALLOWED_HOSTS = [BASE_URL, "127.0.0.1", "localhost"]

    # Debug
    # https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#debug

    DEBUG = True

    # Email URL
    # https://django-configurations.readthedocs.io/en/stable/values/

    EMAIL = values.EmailURLValue("console://")

    # Django Debug Toolbar
    # https://django-debug-toolbar.readthedocs.io/en/stable/configuration.html

    try:
        import debug_toolbar  # noqa
    except ModuleNotFoundError:  # pragma: no cover
        pass
    else:  # pragma: no cover
        INTERNAL_IPS = ["127.0.0.1", "localhost"]
        ProjectDefault.INSTALLED_APPS.append("debug_toolbar")
        ProjectDefault.MIDDLEWARE.append(
            "debug_toolbar.middleware.DebugToolbarMiddleware"
        )


class Alpha(ProjectDefault):
    """The alpha settings."""

    # Security
    # https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#allowed-hosts

    BASE_URL = f"alpha.{ProjectDefault.BASE_HOST_URL}"

    BASE_DOMAIN_URL = f"http://{BASE_URL}"

    ALLOWED_HOSTS = [BASE_URL]

    # Debug
    # https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#debug

    DEBUG = True

    # Email URL
    # https://django-configurations.readthedocs.io/en/stable/values/

    EMAIL = values.EmailURLValue("console://")


class Beta(ProjectDefault):
    """The beta settings."""

    # Security
    # https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#allowed-hosts

    BASE_URL = f"beta.{ProjectDefault.BASE_HOST_URL}"

    BASE_DOMAIN_URL = f"http://{BASE_URL}"

    ALLOWED_HOSTS = [BASE_URL]

    # Debug
    # https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#debug

    DEBUG = False

    # Email URL
    # https://django-configurations.readthedocs.io/en/stable/values/

    EMAIL = values.EmailURLValue("console://")


class Production(ProjectDefault):
    """The production settings."""

    # Security
    # https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#allowed-hosts

    ALLOWED_HOSTS = [ProjectDefault.BASE_URL]

    # Debug
    # https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#debug

    DEBUG = False

    # Email URL
    # https://django-configurations.readthedocs.io/en/stable/values/

    EMAIL = values.EmailURLValue()

    # Deployment
    # https://docs.djangoproject.com/en/{{docs_version}}/howto/deployment/checklist/

    SECURE_BROWSER_XSS_FILTER = True

    SECURE_CONTENT_TYPE_NOSNIFF = True

    X_FRAME_OPTIONS = "DENY"  # Default: 'SAMEORIGIN'

    # CSRF_COOKIE_SECURE = True

    # SECURE_SSL_REDIRECT = True

    # SESSION_COOKIE_SECURE = True

    # SECURE_HSTS_SECONDS = 3600

    # SECURE_HSTS_PRELOAD = True

    # SECURE_HSTS_INCLUDE_SUBDOMAINS = False

    # SECURE_CONTENT_TYPE_NOSNIFF = True

    # SECURE_BROWSER_XSS_FILTER = True

    # CONN_MAX_AGE = None


class Testing(ProjectDefault):
    """The testing settings."""

    # Security
    # https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#allowed-hosts

    ALLOWED_HOSTS = [ProjectDefault.BASE_URL]

    # Debug
    # https://docs.djangoproject.com/en/{{docs_version}}/ref/settings/#debug

    DEBUG = False

    # Email URL
    # https://django-configurations.readthedocs.io/en/stable/values/

    EMAIL = values.EmailURLValue("dummy://")

    # Django REST Framework
    # https://www.django-rest-framework.org/api-guide/settings/

    REST_FRAMEWORK = {}  # type: ignore
