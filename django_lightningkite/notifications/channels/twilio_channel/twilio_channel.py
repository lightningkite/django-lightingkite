from ..channel import Channel
from twilio.rest import Client
from ... import settings
from .exceptions import TwilioSettingNotDefined
from ...signals import sending


class TwilioChannel(Channel):

    def send(notifiable, notification):
        """
        Send the Given Notification

        questions:
        - how generic will this be? do we need to include being
        able to text images and such?

        items of interest:
        - phone numbers
            - phone number that will come from the env
            - phone number we will send a message to

        - message body

        - we can even use a status callback to know whether
        or not it failed or was sent

        """
        if settings.TWILIO_ACCOUNT_SID is None:
            raise TwilioSettingNotDefined('TWILIO_ACCOUNT_SID')
        if settings.TWILIO_AUTH_TOKEN is None:
            raise TwilioSettingNotDefined('TWILIO_AUTH_TOKEN')
        if settings.TWILIO_NUMBER is None:
            raise TwilioSettingNotDefined('TWILIO_NUMBER')

        client = Client(
            settings.TWILIO_ACCOUNT_SID,
            settings.TWILIO_AUTH_TOKEN
        )

        text_message = notification.to_sms(notifiable)

        message_kwargs = text_message.get_kwargs()

        if not hasattr(message_kwargs, 'from_'):
            message_kwargs['from_'] = settings.TWILIO_NUMBER
        if not hasattr(message_kwargs, 'to'):
            if settings.TWILIO_RECEIVE_NUMBER is None:
                raise TwilioSettingNotDefined('TWILIO_RECEIVE_NUMBER')
            message_kwargs['to'] = settings.TWILIO_RECEIVE_NUMBER

        sending.send(sender=TwilioChannel, notifiable=notifiable,
                     notification=text_message)
        message = client.messages.create(**message_kwargs)
        # TODO handle message status/results
        # sent.send(sender=TwilioChannel, notifiable=notifiable, notification=text_message, message=message, status=SUCCESS)
