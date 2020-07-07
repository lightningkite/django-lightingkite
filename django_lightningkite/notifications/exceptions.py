from django.utils.translation import gettext_lazy as _


class NotificationException(Exception):
    """
    Base Exception for django_lightningkite.notifications
    """
    message = _('A Notification Error occured')

    def __init__(self, message, *args):
        if message is not None:
            self.message = message
        super().__init__(self.message, *args)

    def __str__(self):
        return str(self.message)


class InvalidEmailObjectException(NotificationException):
    """
    Object Given is not a valid  django.core.mail.EmailMessage object
    """
    default_message = _('Invalid Email Object')
