from django.contrib import admin

# Register your models here.

from .models import ImagerProfile, Address, Social, CameraType, PhotographyType

admin.site.register(ImagerProfile)
admin.site.register(Address)
admin.site.register(Social)
admin.site.register(CameraType)
admin.site.register(PhotographyType)
