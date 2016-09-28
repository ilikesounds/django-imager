from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def image_view(request):
    return HttpResponse('Fuck You! I\'m a web page!')

def album_view(request):
    return HttpResponse('Fuck You! I\'m a web page!')

def library_view(request):
    return HttpResponse('Fuck You! I\'m a web page!')
