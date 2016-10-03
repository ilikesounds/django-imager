from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from django.views.generic import DetailView
from imager_images.models import Album, Photo

from . import views

urlpatterns = [
    url(r'^library/', views.library_view, name='library_view'),
    url(r'^album/(?P<uuid>[A-Za-z0-9-]*)', views.album_view, name='album_view'),

    # url(r'^album/(?P<uuid>[A-Za-z0-9-]*)',
    #     DetailView.as_view(
    #         model=Album,
    #         template_name='album.html',
    #         pk_url_kwarg='uuid'
    #     ),
    #     name='album_detail'),

    url(r'^(?P<uuid>[A-Za-z0-9-]*)',
        DetailView.as_view(
            model=Photo,
            template_name='photo.html',
            pk_url_kwarg='uuid'
        ),
        name='photo_detail'),
]
