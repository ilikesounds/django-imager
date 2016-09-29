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
        "file_name": my_photo[0].upload,
        "file": os.path.join(MEDIA_ROOT, str(my_photo[0].upload))
    })
    return render(request, 'photo.html', context)
