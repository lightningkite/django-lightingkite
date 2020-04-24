from django.core.mail import EmailMessage

from .channel import Channel


class MailChannel(Channel):

    def send(notifiable, notification):
        """
        Send the Given Notifiction
        """

        message = notification.to_mail(notifiable)

        if isinstance(message, EmailMessage):
            if (hasattr(notification, 'fail_silently')):
                message.send(notifiable.fail_silently)
            else:
                message.send()
