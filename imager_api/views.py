from imager_images.models import Photo
from imager_api.serializers import PhotoSerializer
from rest_framework import generics
from rest_framework import permissions


class PhotoList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated)
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated)
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
