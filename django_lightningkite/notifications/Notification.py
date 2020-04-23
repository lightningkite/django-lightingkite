class Notification():

    def via(self, notifiable):
        return []

    def send(self, notifiable):
        channels = self.via(notifiable)

        print('got herer')
        for channel in channels:
            try:
                print('got herer')
                from . import channel as channel_class
            except expression as identifier:
                raise Exception('{} channel does not exist'.format(channel))
            channel_class.send(notifiable, self)
