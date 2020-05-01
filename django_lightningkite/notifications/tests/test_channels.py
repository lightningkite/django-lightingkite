from django_lightningkite.settings import settings as dl_settings
from django.conf import settings
from django.core.mail import EmailMessage
from django.test import TestCase

from ..notification import Notification
from ..signals import sending, sent
from ..channels.mail_channel import MailChannel
from ..channels.console_channel import ConsoleChannel
from ..channels.database_channel import DatabaseChannel

from ..models import Notification as NotificationModel

# we need to put this somewhere better.
settings_param = dl_settings()
settings_param.update({
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
})
settings.configure(**settings_param)


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
        # return NotificationModel(

        # )
        pass


class DBTests(TestCase):
    def setUp(self):
        self.db_notification = DBNotification()

    def test_db_notify(self):
        sending.connect(self.signal_sending, sender=DatabaseChannel)
        sent.connect(self.signal_sent, sender=DatabaseChannel)
        self.db_notification.send(None)

    def signal_sending(self, sender, **kwargs):
        pass

    def signal_sent(self, sender, **kwargs):
        pass


# class TwilioTests(TestCase):
#     def setUp(self):
#         from ..channels.twilio_channel.text_message import TextMessage
#         from ..channels import TwilioChannel

#         class TextNotification(Notification):
#             def via(self, notifiable):
#                 return ['TwilioChannel']

#             def to_sms(self, notifiable):
#                 text_message = TextMessage(
#                     body="welcome to lightningkite",
#                 )
#                 return text_message

#         self.text_notification = TextNotification()

#     def test_send_text(self):
#         self.text_notification.send(None)
