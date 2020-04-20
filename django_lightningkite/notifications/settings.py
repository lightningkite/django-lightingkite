from django.conf import settings

import environ

env = environ.Env()

TWILIO_ACCOUNT_SID = getattr(
    settings,
    'TWILIO_ACCOUNT_SID,
    env('TWILIO_ACCOUNT_SID'))

TWILIO_AUTH_TOKEN = getattr(
    settings,
    'TWILIO_AUTH_TOKEN,
    env('TWILIO_AUTH_TOKEN'))

TWILIO_NUMBER = getattr(
    settings,
    'TWILIO_NUMBER,
    env('TWILIO_NUMBER'))
