from django.apps import AppConfig


try:
    import yaml
except ImportError as e:
    raise Exception('module pyyaml is missing.')

class StripeConfig(AppConfig):
    name = 'django_lightningkite.stripe'
    verbose_name = 'stripe'
