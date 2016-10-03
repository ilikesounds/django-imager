from django.conf.urls import url
from django.views.generic import DetailView
from imager_images.models import Photo

from . import views

app = 'imager_images'
urlpatterns = [
    url(r'^edit/(?P<uuid>[A-Za-z0-9-]*)',
    views.photo_edit_view,
    name='photo_edit_view'
    ),
    url(r'^(?P<uuid>[A-Za-z0-9-]*)',
        DetailView.as_view(
            model=Photo,
            template_name='photo.html',
            pk_url_kwarg='uuid'
        ),
        name='photo_detail'),
    url(r'^album/', views.album_view, name='album_view'),
    url(r'^library/', views.library_view, name='library_view'),
]

#
