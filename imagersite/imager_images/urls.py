from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^', views.image_view, name='image_view'),
]
