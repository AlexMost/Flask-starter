# -*- coding: utf-8 -*-
"""
Settings module.
"""

import os
current_dir = os.path.dirname(os.path.abspath(__file__))

#Generic app settings.
APP_HOST = "127.0.0.1"
APP_PORT = "5001"
DEBUG = True
TEMPLATE_DIR = os.path.join(current_dir, 'templates')
STATIC_PATH = '/static'

# Database
sqlite_dir = os.path.join(current_dir, 'tmp/test.db')
SQLALCHEMY_DATABASE_URI = "sqlite:////{sqlite_dir}".format(sqlite_dir=sqlite_dir)
