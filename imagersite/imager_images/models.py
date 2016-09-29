from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
import uuid
import datetime
from django.conf import settings

# Create your models here.


def user_directory_path(instance, filename):
    """ This function will return a dynamically generated file path based on
    the user id and the current date for an uploaded photo"""

    return '{}/{}/{}'.format(
        instance.user.id,
        datetime.datetime.today().strftime('%Y-%m-%d'),
        filename,
        )


@python_2_unicode_compatible
class Photo(models.Model):

    PRIVATE, SHARED, PUBLIC = 'Pri', 'Shr', 'Pub'

    PUBLISHED_CHOICES = (
        (PRIVATE, 'Private'),
        (SHARED, 'Shared'),
        (PUBLIC, 'Public')
        )

    photo_id = models.UUIDField(
               primary_key=True,
               default=uuid.uuid4,
               editable=False)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='photo'
        )

    upload = models.ImageField(
        # upload_to=user_directory_path
        upload_to='photos'
        )
    date_created = models.DateTimeField(_('Date Created'), null=True)
    date_modified = models.DateTimeField(_('Date Modified'), auto_now=True)
    date_uploaded = models.DateTimeField(_('Date Uploaded'), auto_now_add=True)
    published_status = models.BooleanField(_('Published Status'))

    lat = models.DecimalField(
        _('Latitude'),
        max_digits=7,
        decimal_places=7,
        null=True,
        blank=True
        )
    lng = models.DecimalField(
        _('Longitude'),
        max_digits=7,
        decimal_places=7,
        null=True,
        blank=True
        )

    camera = models.CharField(_('Camera'), max_length=48, blank=True)
    caption = models.TextField(_('Caption'), blank=True)
    albums = models.ManyToManyField('Album', blank=True)

    def __str__(self):
        """
        This will display in string format the photo object
        """

        photo = str(self.upload)
        return photo


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

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='album'
        )

    date_created = models.DateTimeField(_('Date Created'))
    date_modified = models.DateTimeField(_('Date Modified'), auto_now=True)
    date_uploaded = models.DateTimeField(_('Date Uploaded'), auto_now_add=True)

    album_title = models.CharField(_('Title'), max_length=64, blank=True)
    album_description = models.TextField(_('Description'), blank=True)
    published_status = models.CharField(
        _('Published Status'),
        max_length=3,
        choices=PUBLISHED_CHOICES,
        default=PRIVATE
        )
    cover_photo = models.ForeignKey(
        _('Photo'),
        default=DEFAULT_COVER,
        on_delete=models.SET_DEFAULT, 
        blank=True
        )

    def __str__(self):
        """
        This will display in string format the album object
        """

        album = str(self.album_title)
        return album
