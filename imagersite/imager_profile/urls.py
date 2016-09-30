from django.conf.urls import url
from imager_profile.views import ProfileView


app_name = 'profile_view'
urlpatterns = [
    url(r'^$', ProfileView.as_view(), name='profile_view')
]
