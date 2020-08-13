from . import notification

default_app_config = 'django_lightningkite.notifications.apps.NotificationsConfig'

SUCCESS = 'success'
FAILED = 'failure'

Notification = notification.Notification
