import os
from pathlib import Path
from django_lightningkite.settings import settings

os.environ['DJANGO_SECRET_KEY'] = 'testing.'
BASE_DIR = Path(__file__).parents[2]
vars().update(settings(BASE_DIR))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django_lightningkite.notifications',
]

MIDDLEWARE_CLASSES = ()
