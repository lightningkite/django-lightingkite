from .Channel import Channel


class ConsoleChannel(Channel):

    @staticmethod
    def send(notifiable, notification):
        """
        Send the Given Notifiction
        """

        """
        This class is going to be designed to just throw a notification into the console; this is primarily for testing
        """
        message = notifiable.to_console(notifiable)
        print(notification)


