from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from django.views.generic import CreateView,
from .models import Photo
# Create your views here.


def album_view(request):
    return HttpResponse('Fuck You! I\'m a web page!')


def library_view(request):
    return HttpResponse('Fuck You! I\'m a web page!')


def image_view(request, uuid=None):
    my_photo = Photo.objects.filter(photo_id=uuid)
    context = Context({
        "photo": my_photo,
        "file_name": my_photo.upload,
        "file": my_photo.upload
    })
    return render(request, 'photo.html', context)


class UploadPhotoView(CreateView):
    template_name = 'imager_images/create_photo.html'
    model = Photo
    fields = [
        'upload',
        'user',
        'published_status',
        'camera',
        'caption',
        'album'
        ]
    success_url = '/'
