import os

from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from .models import Photo
from imagersite.settings import BASE_DIR, MEDIA_ROOT
# Create your views here.


def album_view(request):
    return HttpResponse('Fuck You! I\'m a web page!')

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
    return render(request, 'photo.html', context)
