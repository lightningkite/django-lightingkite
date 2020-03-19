
from django.apps import AppConfig

try:
    import yaml
except ImportError as e:
    raise Exception('module pyyaml is missing.')

try:
    import uritemplate
except ImportError as e:
    raise Exception('module uritemplate is missing.')


class DocsConfig(AppConfig):
    name = 'django_lightningkite.docs'
    verbose_name = 'docs'
