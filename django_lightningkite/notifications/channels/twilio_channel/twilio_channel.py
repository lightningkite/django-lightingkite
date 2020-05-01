from ..channel import Channel
from twilio.rest import Client
from ... import settings


class TwilioChannel(Channel):

    def send(notifiable, notification):
        """
        Send the Given Notifiction

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

        client = Client(
            settings.TWILIO_ACCOUNT_SID,
            settings.TWILIO_AUTH_TOKEN
        )

        text_message = notification.to_sms(notifiable)

        message_kwargs = text_message.get_kwargs()

        if not hasattr(message_kwargs, 'from_'):
            message_kwargs['from_'] = settings.TWILIO_NUMBER
        if not hasattr(message_kwargs, 'to'):
            message_kwargs['to'] = settings.TWILIO_RECEIVE_NUMBER

        message = client.messages.create(**message_kwargs)
        # import ipdb; ipdb.set_trace()
