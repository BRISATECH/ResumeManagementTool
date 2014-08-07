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


### mysql new code


ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mysqldb',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'brisa',
        'PASSWORD': 'brisa',
        'HOST': '192.168.1.12',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',                      # Set to empty string for default.
    },

    'rmtdb': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'rmtdb',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'brisa',
        'PASSWORD': 'brisa',
        'HOST': '192.168.1.12',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',     
        }
}



SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'


### end mysql new code




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
#code by akshay
HOTKEYS = [
            
            {'keys': 'alt+m',
            'link': '/RequirementManagement/',
            },
            {'keys': 'alt+s',
            'link': '/requiresub/',
             },
            {'keys': 'alt+r',
            'link': '/resunsub/',
             },
            {'keys': 'alt+f',
            'link': '/searchResult/',
             },
            {'keys': 'alt+f',
            'link': '/query/',
             },
            {'keys': 'alt+q',
            'link': '/logout/',
             },
			 
			 {'keys': 'alt+p',
            'link': '/ReportManagementfile/',
             },
			 {'keys': 'alt+h',
            'link': '/help1/',
             },
            
        ]
#end
		

INSTALLED_APPS = (
    'django.contrib.admin',
#     'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'polls',
	'keyboard_shortcuts',
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


#  SQLITE   DB  COMMENTED

######
######DATABASES = {
######    'default': {
######        'ENGINE': 'django.db.backends.sqlite3',
######        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
######    }
######}



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


### mysql new code

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

### new mysql new code
