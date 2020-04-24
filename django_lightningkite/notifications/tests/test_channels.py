from django.test import TestCase

from ..notification import Notification
# from django_lightningkite.notifications.models import Notification
from ..channels import ConsoleChannel, MailChannel

from django.conf import settings

from ..signals import sending, sent

from django.core.mail import EmailMessage


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


class ConsoleNotification(Notification):
    def via(self, notifiable):
        return ['ConsoleChannel', ConsoleChannel]

    def to_console(self, notifiable):
        return "hello world"


class ConsoleTests(TestCase):

    def setUp(self):
        self.console_notification = ConsoleNotification()

    def test_send_to_console(self):
        sending.connect(self.signal_sending, sender=ConsoleChannel)
        sent.connect(self.signal_sent, sender=ConsoleChannel)
        self.console_notification.send(None)

    def signal_sending(self, sender, **kwargs):
        self.assertIsNone(kwargs.get('notifiable'))
        self.assertIs(self.console_notification, kwargs.get('notification'))

    def signal_sent(self, sender, **kwargs):
        self.assertIsNone(kwargs.get('notifiable'))
        self.assertIs(self.console_notification, kwargs.get('notification'))
        self.assertEqual(kwargs.get('message'), 'hello world')


class EmailNotification(Notification):
    def via(self, notifiable):
        return ['MailChannel']

    def to_mail(self, notifiable):
        # return an email object class
        return EmailMessage(
            'Hello',
            'This is an email',
            'from@fromlightningkite.com',
            ['to@tolightningkite.com']
        )


class EmailTests(TestCase):
    def setUp(self):
        self.email_notification = EmailNotification()

    def test_send_email(self):
        sending.connect(self.signal_sending, sender=MailChannel)
        sent.connect(self.signal_sent, sender=MailChannel)
        # Notifiable will be specified by the user of the library, in our case we don't need one
        self.email_notification.send(None)

    def signal_sending(self, sender, **kwargs):
        self.assertIsNone(kwargs.get('notifiable'))
        self.assertIs(self.email_notification, kwargs.get('notification'))

    def signal_sent(self, sender, **kwargs):
        self.assertIsNone(kwargs.get('notifiable'))
        self.assertIs(self.email_notification, kwargs.get('notification'))
        self.assertEqual(kwargs.get('message').body, 'This is an email')
