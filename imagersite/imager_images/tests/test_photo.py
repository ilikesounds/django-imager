from __future__ import unicode_literals
from django.test import TestCase, override_settings
from imager_images.models import Photo, Album
from imager_images.tests.factories import PhotoFactory, UserFactory
from django.contrib.auth.models import User
import tempfile
import datetime


# Create your tests here.


class PhotoTestCase(TestCase):
    '''This is the test case for the Photo Model'''

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @override_settings(MEDIA_ROOT=tempfile.mkdtemp())
    def test_upload_photo(self):
        new_photo = PhotoFactory()
        photo_dir = 'photo_files'
        user = self.user
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        expected_photo = '/'.join([photo_dir, user, today, 'squirrel.jpg'])
        self.assertEqual(new_photo.upload, expected_photo)


class AlbumTestCase(TestCase):

    def setUp(self):
        pass

    def setUp_user(self):
        user = UserFactory.create()
        user.save()

    def tearDown(self):
        pass

    def test_create_album_with_user(self):
        new_album = Album()
        self.user = UserFactory.create(username="sally")
