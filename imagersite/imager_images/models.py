from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Photo(models.Model):
    
    upload = models.ImageField(upload_to='uploads/') # file will be uploaded to MEDIA_ROOT/uploads
    data_created = models.DateTimeField(_('Date Created'))
    lat = models.DecimalField(_('Latitude'), max_digits=3, decimal_places=7)
    lng = models.DecimalField(_('Longitude'), max_digits=3, decimal_places=7)
    camera = models.CharField(_('File Name'), max_length=48, blank=True)
    caption = models.TextField(_('Caption'), blank=True)
    date_modified = models.DateTimeField(_('Date Modified'), auto_now=True)
    date_uploaded = models.DateTimeField(_('Date Uploaded'), auto_now_add=True)
    publish = models.BooleanField(_('Published'))
    album = models.ManyToMany(Album)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)




@python_2_unicode_compatible
class Photo(models.Model):