from django.conf import settings

import environ

env = environ.Env()

STRIPE_API_KEY = getattr(
    settings,
    'STRIPE_API_KEY',
    env('STRIPE_API_KEY'))

STRIPE_WEBHOOK_SECRET = getattr(
    settings,
    'STRIPE_WEBHOOK_SECRET',
    env('STRIPE_WEBHOOK_SECRET', default=None))

STRIPE_API_VERSION = getattr(
    settings,
    'STRIPE_API_VERSION',
    env('STRIPE_API_VERSION', default=None))
