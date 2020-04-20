from django import dispatch

canceled = dispatch.Signal(providing_args=['notifiable', 'notification'])
scheduled = dispatch.Signal(providing_args=['notifiable', 'notification'])
sending = dispatch.Signal(providing_args=['notifiable', 'notification'])
sent = dispatch.Signal(providing_args=['notifiable', 'notification'])
retrying = dispatch.Signal(providing_args=['notifiable', 'notification'])
failed = dispatch.Signal(providing_args=['notifiable', 'notification'])
success = dispatch.Signal(providing_args=['notifiable', 'notification'])
