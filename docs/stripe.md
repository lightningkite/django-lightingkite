# Stripe Module
## requirements:
 - stripe
 
## usage:

_settings.py_
```python
INSTALLED_APPS = [
    ...
    'django_lightningkite.stripe',
]
```
ensure the STRIPE_API_KEY is set as an enviornemnt variable or a setting.
example usage:
```python
from django_lightningkite.stripe import stripe
stripe.Customer.list()
```

register webhook
_urls.py_
```python
urlpatterns = [
    ...
    path('stripe/', include('django_lightningkite.stripe.urls')),
]
```
