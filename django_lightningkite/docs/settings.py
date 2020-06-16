from django.conf import settings

import environ

env = environ.Env()
if settings.READ_DOT_ENV_FILE:
    env.read_env(settings.ENV_FILE)

PUBLIC_DOCS = getattr(
    settings,
    'PUBLIC_DOCS',
    env.bool('DJANGO_PUBLIC_DOCS', default=False))

DOCS_VERSION = getattr(
    settings,
    'DOCS_VERSION',
    env('DJANGO_DOCS_VERSION', default='0.0.0'))

DOCS_DESCRIPTION = getattr(
    settings,
    'DOCS_DESCRIPTION',
    env('DJANGO_DOCS_DESCRIPTION', default='API for all things'))

DOCS_TITLE = getattr(
    settings,
    'DOCS_TITLE',
    env('DJANGO_DOCS_TITLE', default='Your Project'))
