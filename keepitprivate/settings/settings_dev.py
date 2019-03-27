""" This file define the settings for the development environment """

from keepitprivate.settings.settings import *  # noqa

INSTALLED_APPS += ['django_extensions']  # noqa

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
