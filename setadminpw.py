#!/usr/bin/env python

import os

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'repositext.settings'
django.setup()

from django.contrib.auth.models import User  # noqa E402


if __name__ == '__main__':
    print("  Setting admin user password ...")
    admin_user = User.objects.get(username='admin')
    admin_user.set_password('admin')
    admin_user.save()
    print("  Done.")

