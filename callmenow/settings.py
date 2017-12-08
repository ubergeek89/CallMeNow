"""
Django settings for callmenow project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a^*b=38e%x24wycmeb*wyw&do1q=qn1d&_rrgeo!54a$ii)6ur'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ["*"]
SECURE_REDIRECT_EXEMPT = [r"^widgetapi/",r"^plivo/"]
SECURE_SSL_REDIRECT = True
LOGIN_REDIRECT_URL = '/'
LOGIN_URL='/'
STATIC_ROOT = '/home/callmenow/callmenow_static'
HOME_URL = "app.callmenowhq.com"
#HOME_URL = "127.0.0.1:8000"
#HOME_URL = "8a3c0b62.ngrok.io"
#HOME_URL = "staging.callmenowhq.com"

# Application definition

INSTALLED_APPS = [
    'mainapp.apps.MainappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'mainapp.middleware.SuperAdminMiddleware',
    'mainapp.middleware.TimezoneMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]

ROOT_URLCONF = 'callmenow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'callmenow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES1 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES = {
  'default': {
  'ENGINE': 'django.db.backends.postgresql_psycopg2',
  'NAME': 'callmenow',
  'USER': 'callmenowuser',
  'PASSWORD': 'pass4callmenow',
  'HOST': '162.243.131.92',
  'PORT': '',
  }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

#Number of seconds after which the user will be logged out.
SESSION_COOKIE_AGE = 604800

PLIVO_AUTH_ID = 'MAZJJLMZJLMMQ5MWFHMZ'
PLIVO_AUTH_TOKEN = 'ZTBkZjhhY2M0ZWNkOWFmOTZiZGEzMjM3MDJjZjUx'
POSTMARK_TOKEN = 'a2097480-d252-4c1f-b15a-1bac69c54699'
TRANSACTIONAL_FROM_EMAIL= 'CallMeNow <no-reply@callmenowhq.com>'
FIRSTPROMOTER_APIKEY = '83e7f01fffd9c1b53ed183eeb417fb6d'



#These settings are used for automatic error emails which are sent through SMTP servers provided below
ADMINS = [('Aditya', 'aditya@impulsemedia.co.in')]
MANAGERS = [('Aditya', 'aditya@impulsemedia.co.in')]
SERVER_EMAIL = 'webmaster@callmenowhq.com'

#SMTP Configuration to be used by DJango for sending server error messages
#PostMark
#EMAIL_HOST = 'smtp.postmarkapp.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'a2097480-d252-4c1f-b15a-1bac69c54699'
#EMAIL_HOST_PASSWORD = 'a2097480-d252-4c1f-b15a-1bac69c54699'
#EMAIL_USE_TLS = True

#ElasticEmail
EMAIL_HOST = 'smtp.elasticemail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'aditya@impulsemedia.co.in'
EMAIL_HOST_PASSWORD = '107b1821-551e-46c9-baa0-f21202694f9a'
EMAIL_USE_TLS = True

#Rollbar Configuration
ROLLBAR = {
    'access_token': '241a012818be46e192e072c89fd64b20',
    'environment': 'development' if DEBUG else 'production',
    'branch': 'master',
    'root': '/home/callmenow/callmenow',
}