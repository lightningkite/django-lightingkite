from .channel import Channel


class DatabaseChannel(Channel):

    def send(notifiable, notification):
        """
        Send the Given Notifiction
        """
        message = notification.to_db(notifiable, notification)


        # specify a model that they're going to create and that model's arguments


