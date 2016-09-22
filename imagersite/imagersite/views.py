from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('imagersite/home_page_splash.html')
    context = {}
    return HttpResponse(template.render(context, request))