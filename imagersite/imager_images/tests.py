from __future__ import unicode_literals
from django.test import TestCase
from ..imager_profile.models import ImagerProfile
from .models import Photo, Album
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
import factory

# Create your tests here.


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user{}".format(n))
    email = factory.LazyAttribute(
        lambda x: "{}@example.com".format(x.username)
        )


class AlbumTestCase(TestCase):

    def setUp(self):
        pass

    def setUp_user(self):
        user = UserFactory.create()
        user.save()

    def tearDown(self):
        pass

    def test_upload_photo(self):
        new_photo = Photo()
        new_photo.upload = SimpleUploadedFile(
            name='squirrel.jpg',
            content=open('./squirrel.jpg', 'rb').read(),
            content_type='image/jpeg'
            )
        self.assertEqual(new_photo.upload, 'squirrel.jpg')

    def test_create_album_with_user(self):
        new_album = Album()
        self.user = UserFactory.create(username="sally")
