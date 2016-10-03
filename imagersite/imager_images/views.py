from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
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


def photo_edit_view(request, uuid=None):
    import pdb; pdb.set_trace()
    photo = request.user.photo.get(photo_id=uuid)
    return render(request, 'photo_edit.html')
