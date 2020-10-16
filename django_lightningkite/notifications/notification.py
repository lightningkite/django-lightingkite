from importlib import import_module
import inspect


class Notification():

    def via(self, notifiable, *args, **kwargs):
        return []

    def send(self, notifiable, *args, **kwargs):
        channels = self.via(notifiable, *args, **kwargs)

        for channel in channels:
            if (type(channel) is str):
                try:
                    module = import_module('..channels', package=__name__)
                    channel_class = getattr(module, channel)
                except Exception as e:
                    raise e
                    raise Exception('{} channel does not exist'.format(channel))
            elif inspect.isclass(channel):
                channel_class = channel
            channel_class.send(notifiable, self, *args, **kwargs)
