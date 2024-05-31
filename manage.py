#!/usr/bin/env python

import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
    try:
        from django.core.management.commands.runserver import Command as runserver
        runserver.default_port = os.environ.get('PORT', '8080')
        runserver.default_addr = '0.0.0.0'
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


if __name__ == "__main__":
    main()
