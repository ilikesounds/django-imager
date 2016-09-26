from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    return render(request, 'imagersite/home_page_splash.html')


def logout_view(request):
    pass
