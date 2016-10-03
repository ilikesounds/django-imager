from django.forms import ModelForm
from imager_images.models import Photo

"""All forms needed for editing and adding photos and albums for the
django-imager.imager_images app"""


class PhotoForm(ModelForm):

    """This class handles photo editing by the user"""

    PRIVATE, SHARED, PUBLIC = 'Pri', 'Shr', 'Pub'

    PUBLISHED_CHOICES = (
        (PRIVATE, 'Private'),
        (SHARED, 'Shared'),
        (PUBLIC, 'Public')
        )

    class Meta:
        model = Photo
        fields = ['caption', 'camera', 'albums', 'published_status']
