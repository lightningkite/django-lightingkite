from django.utils.translation import gettext_lazy as _
from ...exceptions import NotificationException


class TwilioSettingNotDefined(NotificationException):
    """
    a twillio setting or env is not defined
    """

    default_message = _('setting or env not defined')

    def __init__(self, message, *args):
        super().__init__("'{}' {}".format(message, self.default_message), *args)
