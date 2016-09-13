from __future__ import unicode_literals

from django.db import models
import uuid

# Create your models here.


class Imager_Profile(models.Model):
    pass


class Address(models.Model):
    street_addr = models.CharField(_('street_addr'), max_length=128)
    unit = models.CharField(_('unit'), max_length=8)
    city = model.CharField(_('city'), max_length=64)
    state = model.CharField(_('state'), max_length=4)
    post_code = model.CharField(_('post_code'), max_length=5)


class Social(models.Model):
    social_type =
    social_type_key =


class Photography_Info(models.Model):
    camera_type =
    photography_type =
