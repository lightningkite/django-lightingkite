from django.core.mail import EmailMessage
from .channel import Channel
from ..signals import sending, sent
from ..exceptions import InvalidEmailObjectException
from .. import SUCCESS, FAILED

class MailChannel(Channel):

    def send(notifiable, notification):
        """
        Send the Given Notifiction
        """

        message = notification.to_mail(notifiable)

        if not isinstance(message, EmailMessage):
            raise InvalidEmailObjectException

        if isinstance(message, EmailMessage):
            if (hasattr(notification, 'fail_silently')):
                message.send(notifiable.fail_silently)
            else:
                sending.send(sender=MailChannel, notifiable=notifiable, notification=notification)
                try:
                    message.send()
                    sent.send(sender=MailChannel, notifiable=notifiable, notification=notification, message=message, status=SUCCESS)
                except Exception as e:
                    sent.send(sender=MailChannel, notifiable=notifiable, notification=notification, message=message, status=FAILED, exception=e)
