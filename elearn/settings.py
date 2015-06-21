"""
Django settings for elearn project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    BASE_DIR + '/templates/',
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = # ???

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False

# LEVEL SCALING AND XP MAX
XP_MAX = 1000
LEVEL_SCALE = 1.5

EMAIL_USE_TLS = True
EMAIL_HOST = # ???
EMAIL_PORT = # ???
EMAIL_HOST_USER = # ???
EMAIL_HOST_PASSWORD = # ???


MEDIA_ROOT = BASE_DIR + '/media/'
MEDIA_URL = '/media/'

SOLUTION = BASE_DIR + '/challenge/solutions/'

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lessons',
    'registration'
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

ROOT_URLCONF = # ???

WSGI_APPLICATION = # ???

DATABASES = {
    'default': {
        'ENGINE': # ???,
        'NAME': # ???,
        'HOST': # ???,
        'PORT': # ???,
        'USER': # ???,
        'PASSWORD': # ???
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/elearn/static',
)
STATIC_URL = '/static/'