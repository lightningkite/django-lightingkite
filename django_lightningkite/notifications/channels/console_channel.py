from .channel import Channel
import sys
from ..signals import sending, sent
from .. import SUCCESS, FAILED


class ConsoleChannel(Channel):

    @staticmethod
    def send(notifiable, notification, *args, **kwargs):
        """
        Send the Given Notifiction
        """

        """
        This class is going to be designed to just throw a notification into the console; this is primarily for testing
        """
        sending.send(sender=ConsoleChannel, notifiable=notifiable, notification=notification)
        # TODO make thread safe: https://github.com/django/django/blob/master/django/core/mail/backends/console.py
        message = notification.to_console(notifiable, *args, **kwargs)
        sys.stdout.write('{}\n'.format(message))
        sent.send(sender=ConsoleChannel, notifiable=notifiable, notification=notification, message=message, status=SUCCESS)
