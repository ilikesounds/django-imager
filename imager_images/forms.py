from django.forms import ModelForm
from django import forms
from imager_images.models import Album, Photo

"""All forms needed for editing and adding photos and albums for the
django-imager.imager_images app"""


class PhotoUploadForm(ModelForm):

    """This custom class overrides the widgets for the UploadPhotoView form
       model.
    """

    class Meta:
        model = Photo
        fields = ['upload', 'caption', 'camera', 'albums', 'published_status']
        widgets = {
            'published_status': forms.Select(attrs={'class': 'mdb-select'}),
            'albums': forms.SelectMultiple(attrs={
                'class': 'mdb-select',})
        }

class NewAlbumForm(ModelForm):

    """This custom class overrides the widgets for the UploadPhotoView form
       model.
    """

    class Meta:
        model = Album
        fields = ['album_title', 'album_description', 'published_status']
        widgets = {
            'published_status': forms.Select(attrs={'class': 'mdb-select'}),
        }


class PhotoEditForm(ModelForm):

    """This custom class overrides the widgets for the UploadPhotoView form
       model.
    """

    class Meta:
        model = Photo
        fields = ['caption', 'camera', 'albums', 'published_status']
        widgets = {
            'published_status': forms.Select(attrs={'class': 'mdb-select'}),
            'albums': forms.SelectMultiple(attrs={
                'class': 'mdb-select',})
        }
