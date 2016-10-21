import factory
from django.contrib.auth.models import User
from imager_images.models import Photo
import os

RESOURCES = os.path.join(os.path.dirname(__file__), 'resources')

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user{}".format(n))
    email = factory.LazyAttribute(
        lambda x: "{}@example.com".format(x.username)
        )


class PhotoFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Photo

    user = factory.SubFactory(UserFactory)

    upload = factory.django.ImageField(
        # filename='test_image.jpg',
        from_path=os.path.join(RESOURCES, 'squirrel.jpg')
        # # width=1600,
        # # height=900,
        # color='grey'
        )

    published_status = False
