""" This file define the settings for the development environment """

from keepitprivate.settings.settings import *  # noqa

INSTALLED_APPS += ['django_extensions']  # noqa

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# For development purposes, we are adding basic and session auth to be able to
# play around with the api browser
REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] += (  # noqa
    'rest_framework.authentication.BasicAuthentication',
    'rest_framework.authentication.SessionAuthentication',
)
