from django.test import TestCase

from ..notification import Notification
# from django_lightningkite.notifications.models import Notification
from ..channels import ConsoleChannel

from django.conf import settings


# we need to put this somewhere better.
settings.configure(DEBUG=True,
                   DATABASES={
                       'default': {
                           'ENGINE': 'django.db.backends.sqlite3',
                       }
                   },
                   INSTALLED_APPS=('django.contrib.auth',
                                   'django.contrib.contenttypes',
                                   'django.contrib.sessions',
                                   'django.contrib.admin',
                                   'django_lightningkite.notifications',))


def test_foo():
    """
    example of non django (pytest) test.
    delete me.
    """
    assert 3 == 3


class ConsoleNotification(Notification):
    def via(self, notifiable):
        return ['ConsoleChannel', ConsoleChannel]

    def to_console(self, notifiable):
        return "hello world"


class ConsoleTests(TestCase):

    # what is the difference between the model in the database and the notification class?
    def setUp(self):
        self.console_notification = ConsoleNotification()

    def test_send_to_console(self):
        self.console_notification.send(None)
        # we could use the signal to make sure it sent :o
