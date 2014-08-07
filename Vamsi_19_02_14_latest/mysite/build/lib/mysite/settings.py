"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i7i^))m7(jkd*(jjslh9xak&qwph$)xe0unkhnt+7)!r_p6bzr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
EMAIL_USE_TLS=('586')
EMAIL_HOST=('smtp.gmail.com')
EMAIL_PORT=('587')
EMAIL_HOST_USER=('brisatechnology@gmail.com')
EMAIL_HOST_PASSWORD=("brisa123")

##EMAIL_HOST_USER=('gauravbrisa@gmail.com')
##EMAIL_HOST_PASSWORD=("brisa4jun")



# EMAIL_USE_TLS=True
ALLOWED_HOSTS = []
TEMPLATE_LOADERS = (
   'django.template.loaders.filesystem.Loader',
   'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

import os
path = os.getcwd()+r"\template_html"
TEMPLATE_DIRS =(path)
#django.core.mail.backends.smtp.EmailBackend
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
#     'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.core.mail.backends.smtp.EmailBackend',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
