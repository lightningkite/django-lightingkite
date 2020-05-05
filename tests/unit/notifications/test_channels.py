import os

import django
from django.core.mail import EmailMessage
from django.test import TestCase

from django_lightningkite.notifications import Notification
from django_lightningkite.notifications.signals import sending, sent

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.unit.settings')
django.setup()

from django_lightningkite.notifications.models import Notification as NotificationModel
from django_lightningkite.notifications.channels import ConsoleChannel, DatabaseChannel, MailChannel


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


class DBNotification(Notification):
    def via(self, notifiable):
        return ['DatabaseChannel']

    def to_db(self, notifiable):
        # create an instance of the model Notification, but do not save it
        from django.contrib.contenttypes.models import ContentType
        from django.contrib.auth.models import User
        content_type = ContentType.objects.get(model='user')
        return NotificationModel(
            recipient=User.objects.first(),
            actor_content_type=content_type,
            actor_object_id=notifiable.id,
            verb="notified",
        )


class DBTests(TestCase):
    def setUp(self):
        from django.contrib.auth.models import User
        self.db_notification = DBNotification(

        )
        self.first_user = User.objects.create(
            first_name="first",
            username="first_user"
        )
        self.second_user = User.objects.create(
            first_name="second",
            username="second_user"
        )

    def test_db_notify(self):
        sending.connect(self.signal_sending, sender=DatabaseChannel)
        sent.connect(self.signal_sent, sender=DatabaseChannel)
        self.db_notification.send(self.second_user)

    def signal_sending(self, sender, **kwargs):
        self.assertFalse(NotificationModel.objects.exists())

    def signal_sent(self, sender, **kwargs):
        self.assertTrue(NotificationModel.objects.exists())
