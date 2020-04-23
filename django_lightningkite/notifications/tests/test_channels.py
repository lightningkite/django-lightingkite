from django.test import TestCase

from django_lightningkite.notifications.Notification import Notification
# from django_lightningkite.notifications.models import Notification
from django_lightningkite.notifications.channels import ConsoleChannel

class ConsoleNotification(Notification):
    def via(notifiable):
        return ['ConsoleChannel', ConsoleChannel.__class__]
    def to_console(notifiable):
        return "hello {}".format(notifiable.name)

class ConsoleTests(TestCase):
    # what is the difference between the model in the database and the notification class? 
    def setUp(self):
        self.console_notification = ConsoleNotification()
        self.console_notification.send()
    
    def test_send_to_console(self):
        pass
        # make your instance of the channel and then fire of its send function....? 
