django-lightningkite
==============
a common package for lightningkite projects

<!-- **Document contents**

- [Installation](#installation) -->

# Installation

#### Dependencies
* [Django](https://www.djangoproject.com/)

### Installation
Run the following commands:
http
```bash
pip install git+https://github.com/lightningkite.com/django-lightingkite
                                or
pip install git+ssh://github.com/lightningkite.com/django-lightingkite
```

import base settings
```python
from django_lightningkite.settings import env, settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
vars().update(settings(BASE_DIR))
```
