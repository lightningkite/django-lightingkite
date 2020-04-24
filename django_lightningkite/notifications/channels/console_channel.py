from .channel import Channel
import sys


class ConsoleChannel(Channel):

    @staticmethod
    def send(notifiable, notification):
        """
        Send the Given Notifiction
        """

        """
        This class is going to be designed to just throw a notification into the console; this is primarily for testing
        """
        # TODO make thread safe: https://github.com/django/django/blob/master/django/core/mail/backends/console.py
        message = notification.to_console(notifiable)
        sys.stdout.write('{}\n'.format(message))
