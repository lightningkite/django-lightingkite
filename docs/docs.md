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
