from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.conf import settings


class AbstractNotification(models.Model):
    """
    model describing the actor acting out a verb (on an optional target).
    Generalized Format::
        <actor> <verb> <time>
        <actor> <verb> <target> <time>
        <actor> <verb> <action_object> <target> <time>
    Examples::
        <justquick> <reached level 60> <1 minute ago>
        <brosner> <commented on> <pinax/pinax> <2 hours ago>
        <washingtontimes> <started follow> <justquick> <8 minutes ago>
        <mitsuhiko> <closed> <issue 70> on <mitsuhiko/flask> <about 2 hours ago>
    Unicode Representation::
        justquick reached level 60 1 minute ago
        mitsuhiko closed issue 70 on mitsuhiko/flask 3 hours ago

    based on::
    https://github.com/django-notifications/django-notifications/blob/master/notifications/base/models.py
    """
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=False,
        related_name='notifications',
        on_delete=models.CASCADE
    )

    actor_content_type = models.ForeignKey(
        ContentType, related_name='notify_actor', on_delete=models.CASCADE)
    actor_object_id = models.CharField(max_length=255)
    actor = GenericForeignKey('actor_content_type', 'actor_object_id')

    verb = models.CharField(max_length=256)
    body = models.TextField(blank=True, null=True)

    target_content_type = models.ForeignKey(
        ContentType,
        related_name='notify_target',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    target_object_id = models.CharField(max_length=255, blank=True, null=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')

    action_object_content_type = models.ForeignKey(
        ContentType,
        blank=True,
        null=True,
        related_name='notify_action_object',
        on_delete=models.CASCADE)
    action_object_object_id = models.CharField(
        max_length=255, blank=True, null=True)
    action_object = GenericForeignKey(
        'action_object_content_type', 'action_object_object_id')

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        ctx = {
            'actor': self.actor,
            'verb': self.verb,
            'action_object': self.action_object,
            'target': self.target,
            'timesince': self.timesince()
        }
        if self.target:
            if self.action_object:
                return u'%(actor)s %(verb)s %(action_object)s on %(target)s %(timesince)s ago' % ctx
            return u'%(actor)s %(verb)s %(target)s %(timesince)s ago' % ctx
        if self.action_object:
            return u'%(actor)s %(verb)s %(action_object)s %(timesince)s ago' % ctx
        return u'%(actor)s %(verb)s %(timesince)s ago' % ctx

    def timesince(self, now=None):
        """
        Shortcut for the ``django.utils.timesince.timesince`` function of the
        current timestamp.
        """
        from django.utils.timesince import timesince as timesince_
        return timesince_(self.timestamp, now)

    class Meta:
        abstract = True
        ordering = ('-timestamp',)


class Notification(AbstractNotification):

    class Meta(AbstractNotification.Meta):
        abstract = False
