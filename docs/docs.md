# docs module 
## requirements:
 - pyyaml
 - django-rest-framework >= 3.10
 - uritemplate
 
## usage:

_settings.py_
```python
INSTALLED_APPS = [
    ...
    'django_lightningkite.docs',
]
```

_urls.py_
```python
urlpatterns = [
    ...
    path('docs/', include('django_lightningkite.docs.urls')),
]
```

## available env variables.

DJANGO_PUBLIC_DOCS=False
DJANGO_DOCS_VERSION=0.0.0
DJANGO_DOCS_DESCRIPTION=API for all things
DJANGO_DOCS_TITLE=Your Project

## available settings.
PUBLIC_DOCS=False
DOCS_VERSION=0.0.0
DOCS_DESCRIPTION=API for all things
DOCS_TITLE=Your Project