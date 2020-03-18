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
