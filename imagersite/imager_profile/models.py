from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import uuid

# Create your models here.


class Imager_Profile(models.Model):
    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        fn = self.user.get_full_name().strip() or self.user.get_username()
        return "{}: {}".format(fn, self.card_number)



class Address(models.Model):
    imager_profile = models.ForeignKey(
        Imager_Profile,
        on_delete=models.CASCADE,
        primary_key=True)
    street_addr = models.CharField(_('street_addr'), max_length=128)
    unit = models.CharField(_('unit'), max_length=8)
    city = models.CharField(_('city'), max_length=64)
    state = models.CharField(_('state'), max_length=4)
    post_code = models.CharField(_('post_code'), max_length=5)


class Social(models.Model):
    imager_profile = models.ForeignKey(
        Imager_Profile,
        on_delete=models.CASCADE,
        primary_key=True)
    social_type = models.CharField(_('social_type'), max_length=64)
    social_url = models.CharField(_('social_url'), max_length=64)


class Camera_Type(models.Model):
    imager_profile = models.ForeignKey(
        Imager_Profile,
        on_delete=models.CASCADE,
        primary_key=True)
    camera_type = models.CharField(_('camera_type'), max_length=64)

class Photography_Type(models.Model):
    imager_profile = models.ForeignKey(
        Imager_Profile,
        on_delete=models.CASCADE,
        primary_key=True)
    photography_type = models.CharField(_('photography_type'), max_length=32)
