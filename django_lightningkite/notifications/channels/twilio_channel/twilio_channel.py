from .channel import Channel
from twilio.rest import Client
from ... import settings


class TwilioChannel(Channel):

    def send(notifiable, notification):
        """
        Send the Given Notifiction

        questions:
        - how generic will this be? do we need to include being able to text images and such? 
        
        items of interest:
        - phone numbers
            - phone number that will come from the env
            - phone number we will send a message to
        
        - message body

        - we can even use a status callback to know whether or not it failed or was sent

        """

        client = Client(settings.TWILIO_SID, settings.TWILIO_TOKEN)

        text_message = notification.to_sms()

        message_kwargs = text_message.get_kwargs()

        message = client.messages.create(message_kwargs)

