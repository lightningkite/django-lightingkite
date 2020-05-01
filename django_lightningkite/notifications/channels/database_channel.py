from .channel import Channel
from django.db import models


class DatabaseChannel(Channel):

    def send(notifiable, notification):
        """
        Send the Given Notifiction
        """
        message = notification.to_db(notifiable)

        if isinstance(message, models.Model):
            message.save()
