# Custom user models

## AbstractBaseEmail
    this is an abstract user that is setup to have no username only an mail for authentication.
    
### useage:
insure that the model is installed in your INSTALLED_APPS and that the AUTH_USER_MODEL setting is set to your model. Then you can run `python manage.py makemigrations`
_users/models.py_
```python
from django_lightningkite.users.models import AbstractEmailUser


class User(AbstractEmailUser):
    pass

```
_users/admin.py_
```python
from django_lightningkite.users.models import AbstractEmailUser


class User(AbstractEmailUser):
    from django.contrib import admin
    from django_lightningkite.users.admin import EmailUserAdmin
    from .models import User


    @admin.register(User)
    class UserAdmin(EmailUserAdmin):
        pass
```

if you are using django_rest_framework the bellow settings can be used for the EmailUser

```python
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'django_lightningkite.users.serializers.EmailRegisterSerializer',
}

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'django_lightningkite.users.serializers.EmailUserDetailsSerializer',
    'LOGIN_SERIALIZER': 'django_lightningkite.users.serializers.EmailUserLoginSerializer',
}
```
