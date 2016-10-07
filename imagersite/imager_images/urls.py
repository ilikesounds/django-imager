from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from imager_images.views import (PhotoView,
                                 UploadPhotoView,
                                 NewAlbumView,
                                 AlbumDetailView,
                                 LibraryView
                                 )

app = 'imager_images'
urlpatterns = [
    url(
        r'^photos/new/$',
        login_required(UploadPhotoView.as_view()),
        name='upload_photo'
        ),
    url(
        r'^photos/(?P<pk>[A-Za-z0-9-]*)/$',
        PhotoView.as_view(),
        name='photos_detail'
        ),
    url(
        r'^albums/new/$',
        login_required(NewAlbumView.as_view()),
        name='new_album'
        ),
    url(
        r'^albums/(?P<pk>[A-Za-z0-9-]*)/$',
        AlbumDetailView.as_view(),
        name='album_detail'
        ),
    url(r'library/$',
        LibraryView.as_view(),
        name='library_view'
        )
]
