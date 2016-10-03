import os

from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from django.views.generic import TemplateView
from .models import Album, Photo
from imagersite.settings import BASE_DIR, MEDIA_ROOT
# Create your views here.


def album_view(request, uuid=None):
    my_album = Album.objects.get(album_id=uuid)
    query_photos = Photo.objects.all()
    # TODO: querry photos on album.
    numb_of_pics = len(query_photos)
    one_photo = query_photos.first()
    context = Context({
        "album": my_album,
        "numb_of_pics": numb_of_pics,
        "image": one_photo,
    })
    return render(request, 'imager_images/album.html', context)

def library_view(request):
    return HttpResponse('Fuck You! I\'m a web page!')

def image_view(request, uuid=None):
    import pdb; pdb.set_trace()
    my_photo = Photo.objects.filter(photo_id=uuid)
    context = Context({
        "photo": my_photo,
        "file_name": my_photo.upload,
        "file": my_photo.upload
    })
    return render(request, 'imager_images/photo.html', context)

