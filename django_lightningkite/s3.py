from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticRootS3Storage(S3Boto3Storage):
    location = settings.AWS_STATIC_LOCATION


class MediaRootS3Storage(S3Boto3Storage):
    location = settings.AWS_MEDIA_LOCATION
