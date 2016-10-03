from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView
from .models import Photo, Album
from django.urls import reverse
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


class PhotoView(DetailView):
    pass


class AlbumView(DetailView):
    pass


class AlbumDetailView(DetailView):
    pass


class UploadPhotoView(CreateView):
    template_name = 'imager_images/create_photo.html'
    model = Photo
    fields = [
        'upload',
        'user',
        'published_status',
        'camera',
        'caption',
        'albums'
        ]

    def get_success_url(self):
        url = self.object.upload.url
        return url
