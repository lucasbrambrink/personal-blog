"""
Django settings for personal_blog project.

"""

import os
import socket
DEBUG = False if socket.gethostname() == '192.168.1.2' or socket.gethostname() == 'Lucass-MBP' else True

if DEBUG:  # not-production
    PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
else:  # production-settings
    PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


ALLOWED_HOSTS = []


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'base',
    'home',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'personal_blog.urls'

###---< Email Config >---###
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'


WSGI_APPLICATION = 'personal_blog.wsgi.application'


###---< Database >---###

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog',
        'USER': 'lb',
        'PASSWORD': 'Jackson',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        }
}

###---< Internationalization >---###

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


###---< Static files >---###
BASE_DIR = os.path.join(PROJECT_DIR, 'base')
HOME_DIR = os.path.join(PROJECT_DIR, 'home')

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'root')
MEDIA_ROOT = BASE_DIR + '/media/'

STATICFILES_DIRS = (
    ('base', os.path.join(BASE_DIR, 'static/bower_components')),
    ('home', os.path.join(HOME_DIR, 'static'))
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'static/templates'),
    os.path.join(HOME_DIR, 'static/templates'),
)


# PRODUCTION_LINK = 'https://blog.herokuapp.com'


###---< Import Local Settings >---###
if DEBUG:
    try:
        from local_settings import *
    except ImportError:
        raise 'Unable to import local settings file'

###---< Production Settings >---###
else:
    try:
        from production_settings import *
    except ImportError:
        raise 'Unable to load production settings'

