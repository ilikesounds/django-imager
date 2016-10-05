from django.forms import ModelForm
from django import forms
from imager_images.models import Photo

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


