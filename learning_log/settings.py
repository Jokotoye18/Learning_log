"""
Django settings for learning_log project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url
from decouple import config
from decouple import Csv
import django_heroku
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# sentry_sdk.init(
#     dsn= config('SENTRY_DSN'),
#     integrations=[DjangoIntegration()],
# )


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '6$5l#8o0!+ld632@mpiano9)2)#makjn+kkg72ke)$u!=48b#1'
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1', cast=Csv())

ENVIRONMENT = config('ENVIRONMENT', default='production')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',


    #django allauth
    'allauth', 
    'allauth.account', 
    'allauth.socialaccount', 

    #third party app
    'crispy_forms',
    'debug_toolbar',
    'sri',


    ##############
    #'allauth.socialaccount.providers.facebook', 
    'allauth.socialaccount.providers.github', 
    'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.twitter', 

    #local app
    'logs',
    'pages',
    'profiles',
    
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #Whitenoise
    'django.middleware.common.CommonMiddleware',
    'django.middleware.common.CommonMiddleware', 
    # 'csp.middleware.CSPMiddleware',# django-csp
    'debug_toolbar.middleware.DebugToolbarMiddleware', #debug-toolbar
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'learning_log.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'learning_log.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASE_URL = config('DATABASE_URL')
# db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)
# DATABASES['default'].update(db_from_env)

SITE_ID = 1

#debug-toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]


AUTHENTICATION_BACKENDS  = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True






# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

LOGIN_REDIRECT_URL = 'logs:log_topic_list'
ACCOUNT_LOGOUT_REDIRECT = 'page:home' 



ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE =  True 
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True 
ACCOUNT_USERNAME_REQUIRED  = True
ACCOUNT_UNIQUE_USERNAME = True 



# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')


DEFAULT_FROM_EMAIL = 'Learning log <jokotoyeademola995@gmail.com>'

ADMIN  = (
    ('Jokotoye Ademola', 'jokotoyeademola995@gmail.com'),
)

MANAGER = ADMIN

# # Keep our policy as strict as possible
# CSP_DEFAULT_SRC = ("'none'",)
# CSP_STYLE_SRC = ("'self'", 'fonts.googleapis.com')
# CSP_SCRIPT_SRC = ("'self'",)
# CSP_FONT_SRC = ("'self'", 'fonts.gstatic.com')
# CSP_IMG_SRC = ("'self'",)

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

if ENVIRONMENT == 'production':
    CACHE = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache', 
            'LOCATION': '127.0.0.1:11211',
            'OPTIONS': {
                'server_max_value_length': 1024 * 1024 * 2,
            }
        }
    }
    
    #HTTP Strict Transport Security (HSTS)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 15768000
    SECURE_HSTS_PRELOAD = True

    #Cross-Site Request Forgery (CSRF)
    CSRF_COOKIE_SECURE = True  # cookie will only be sent over an HTTPS connection
    CSRF_COOKIE_HTTPONLY = True  # only accessible through http(s) request, JS not allowed to access csrf cookies

    
    X_FRAME_OPTIONS = 'DENY'
    # SECURE_REFERRER_POLICY = 'same-origin'
    
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    #Cross-Site Scripting (XSS)
    SECURE_BROWSER_XSS_FILTER = True
    SESSION_COOKIE_HTTPONLY = True
    #django-csp(Details at official docs)


# django_heroku.settings(locals())