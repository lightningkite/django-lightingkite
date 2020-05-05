import django
from django.conf import settings
from django.test import TestCase

from django_lightningkite.notifications import Notification
from django_lightningkite.settings import settings as dl_settings

# we need to put this somewhere better.
settings_param = dl_settings()
settings_param.update({
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    'INSTALLED_APPS': {
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'django_lightningkite.notifications',
    }
})

settings.configure(**settings_param)
django.setup()


class TwilioTests(TestCase):
    def setUp(self):
        from django_lightningkite.notifications.channels.twilio_channel.text_message import TextMessage

        class TextNotification(Notification):
            def via(self, notifiable):
                return ['TwilioChannel']

            def to_sms(self, notifiable):
                text_message = TextMessage(
                    body="welcome to lightningkite",
                )
                return text_message

        self.text_notification = TextNotification()

    def test_send_text(self):
        self.text_notification.send(None)
