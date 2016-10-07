from rest_framework import serializers
from imager_images.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = (
            'photo_id',
            'user',
            'upload',
            'date_created',
            'date_modified',
            'date_uploaded',
            'published_status',
            'lat',
            'lng',
            'camera',
            'caption',
        )

