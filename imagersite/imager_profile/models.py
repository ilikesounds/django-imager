
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _

import uuid

# Create your models here.

@python_2_unicode_compatible
class ImageProfileManager(models.Manager):

    class Meta:
        model = 'ImagerProfile'

    def get_queryset(self):
        qs = super(ImageProfileManager, self).get_queryset()
        return qs.filter(user__is_active=True)


@python_2_unicode_compatible
class ImagerProfile(models.Model):

    objects = models.Manager()

    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        fn = self.user.get_full_name().strip() or self.user.get_username()
        return "{}".format(fn)

    active = ImageProfileManager()

    @property
    def active(self):
        return self.user.is_active


@python_2_unicode_compatible
class Address(models.Model):
    imager_profile = models.ForeignKey(
        ImagerProfile,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='address')
    street_addr = models.CharField(_('Street Address'), max_length=128, blank=True)
    unit = models.CharField(_('Unit'), max_length=8, blank=True)
    city = models.CharField(_('City'), max_length=64, blank=True)
    state = models.CharField(_('state'), max_length=4, blank=True)
    post_code = models.CharField(_('Postal Code'), max_length=5, blank=True)


@python_2_unicode_compatible
class Social(models.Model):
    imager_profile = models.ForeignKey(
        ImagerProfile,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='social')
    social_type = models.CharField(_('Social Medial Type'), max_length=64, blank=True)
    social_url = models.CharField(_('Social Media URL'), max_length=64, blank=True)


@python_2_unicode_compatible
class CameraType(models.Model):
    imager_profile = models.ForeignKey(
        ImagerProfile,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='camera_type')
    camera_type = models.CharField(_('Camera Type'), max_length=64, blank=True)


@python_2_unicode_compatible
class PhotographyType(models.Model):
    PHOTOGRAPHY_CHOICES = (
        ('Nature', 'Nature'),
        ('Portrait', 'Portrait'),
        ('Family', 'Family'),
        ('Urban', 'Urban'),
        ('Astronomy', 'Astronomy'),
    )
    imager_profile = models.ForeignKey(
        ImagerProfile,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='photography_type')
    photography_type = models.CharField(_('Photography Type'), max_length=32, choices=PHOTOGRAPHY_CHOICES)
