from django.conf.urls import url
from django.conf.urls import include
from imager_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^v1$', views.PhotoList.as_view()),
    url(r'^v1/(?P<pk>[A-Za-z0-9-]*)$', views.PhotoDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
