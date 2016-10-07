from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from imager_profile.views import ProfileView


app_name = 'profile_view'
urlpatterns = [
    url(r'^$', login_required(ProfileView.as_view()), name='profile_view')
]
