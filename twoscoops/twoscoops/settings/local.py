from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'twoscoops',
        'HOST': 'localhost',
        'USER': 'quixom',
        'PASSWORD': 'root',
    }
}

INSTALLED_APPS += ['debug_toolbar',]
