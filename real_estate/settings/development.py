from django.conf.global_settings import (
    DEFAULT_FROM_EMAIL,
    EMAIL_BACKEND,
    EMAIL_HOST_USER,
)
from .base import *

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_USE_TLS = True
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = "alissonof@uol.com.br"
DOMAIN = env("DOMAIN")
SITE_NAME = "REAL ESTATE"

# DATABASES = {
#     "default": {
#     'ENGINE': 'django.db.backends.sqlite3',
#     'NAME': os.path.join(SITE_ROOT, 'database.sqlite')
#     }
# }


DATABASES = {
    "default": {
        "ENGINE": env("POSTGRES_ENGINE"),
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("PG_HOST"),
        "PORT": env("PG_PORT"),
    }
}

CELERY_BROKER_URL = env("CELERY_BROKER")
CELERY_RESULT_BACKEND = env("CELERY_BACKEND")
CELERY_TIMEZONE = "America/Sao_Paulo"
