from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
import uuid

# Create your models here.

@python_2_unicode_compatible
class Photo(models.Model):

    PRIVATE, SHARED, PUBLIC = 'Pri', 'Shr', 'Pub'

    PUBLISHED_CHOICES = (
    (PRIVATE, 'Private'),
    (SHARED, 'Shared'),
    (PUBLIC, 'Public')
    )

    def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}/{1}'.format(instance.user.id, filename)

    photo_id = models.UUIDField(
               primary_key=True,
               default=uuid.uuid4,
               editable=False)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    upload = models.ImageField(upload_to='photo_files/%Y-%m-%d') # file will be uploaded to MEDIA_ROOT/uploads
    date_created = models.DateTimeField(_('Date Created'))
    date_modified = models.DateTimeField(_('Date Modified'), auto_now=True)
    date_uploaded = models.DateTimeField(_('Date Uploaded'), auto_now_add=True)
    published_status = models.BooleanField(_('Published Status'))

    lat = models.DecimalField(_('Latitude'), max_digits=3, decimal_places=7)
    lng = models.DecimalField(_('Longitude'), max_digits=3, decimal_places=7)

    camera = models.CharField(_('Camera'), max_length=48, blank=True)
    caption = models.TextField(_('Caption'), blank=True)
    album = models.ManyToMany('Album')


@python_2_unicode_compatible
class Album(models.Model):

    PRIVATE, SHARED, PUBLIC = 'Pri', 'Shr', 'Pub'
    PUBLISHED_CHOICES = (
    (PRIVATE, 'Private'),
    (SHARED, 'Shared'),
    (PUBLIC, 'Public')
    )

    DEFAULT_COVER = None

    album_id = models.UUIDField(
               primary_key=True,
               default=uuid.uuid4,
               editable=False)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, default=DEFAULT_COVER, on_delete=models.CASCADE)

    date_created = models.DateTimeField(_('Date Created'))
    date_modified = models.DateTimeField(_('Date Modified'), auto_now=True)
    date_uploaded = models.DateTimeField(_('Date Uploaded'), auto_now_add=True)

    album_title = models.CharField(_('Title'), max_length=64, blank=True)
    album_description = models.TextField(_('Description'), blank=True)
    published_status = models.CharField(_(max_length=3, choices=PUBLISHED_CHOICES, default=PRIVATE))
    cover_photo = models.ForeignKey('Photo', on_delete=models.SET_DEFAULT)
