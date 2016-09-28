from django.contrib.auth import views
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from imager_images.models import Photo
from registration.backends.hmac.views import RegistrationView
from django.views.generic.base import TemplateView
from django.urls import reverse


class NewRegView(RegistrationView):
    """If the user is logged in, this view will redirect them"""
    def get(self, request):
        if request.user.is_authenticated():
            return render(request, reverse('profile'))
        return super().get(request)

    def post(self, request):
        return views.login(request)

class NewLoginView(TemplateView):
    pass


def index(request):
    # if request.user.is_authenticated:
    #     photo = Photo.objects.filter(query).order_by('?').first()

    return render(request, 'imagersite/home_page_splash.html')

