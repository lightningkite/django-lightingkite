from setuptools import setup

version = __import__('django_lightningkite').__version__

setup(
    version=version,
    install_requires=[
        "Django>=2",
        "django-environ>=0.4.5,<1.0.0",
        "sentry-sdk>=0.13.0,<1.0.0",
    ],
)
