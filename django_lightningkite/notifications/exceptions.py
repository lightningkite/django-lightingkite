from django.utils.translation import gettext_lazy as _

class NotificationException(Exception):
    """
    Base Exception for django_lightningkite.notifications
    """
    default_detail = _('A Notification Error occured')

    def __init__(self, detail=None):
        if detail is None:
            detail = self.default_detail

    def __str__(self):
        return str(self.detail)


class InvalidEmailObjectException(NotificationException):
    """
    Object Given is not a valid  django.core.mail.EmailMessage object
    """
    default_detail = _('Invalid Email Object')
