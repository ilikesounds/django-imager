from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^', views.image_view, name='image_view'),
    url(r'^album/', views.album_view, name='album_view'),
    url(r'^library/', views.library_view, name='library_view'),
]
