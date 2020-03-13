import os
import re

from setuptools import setup

version = __import__('django_lightningkite').__version__


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)

setup(
    version=get_version('django_lightningkite'),
    install_requires=[
        "Django>=2",
        "django-environ>=0.4.5,<1.0.0",
        "sentry-sdk>=0.13.0,<1.0.0",
    ],
)
