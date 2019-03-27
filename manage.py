#!/usr/bin/env python
import os
import sys

from keepitprivate.constants import DEV, PROD

if __name__ == '__main__':
    environment = os.environ.get('KIP_ENV', DEV)

    if environment == PROD:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'keepitprivate.settings.settings')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'keepitprivate.settings.settings_dev')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
