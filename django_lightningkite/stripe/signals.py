from django import dispatch

stripe_webhook = dispatch.Signal(providing_args=['event', 'request'])
