from __future__ import unicode_literals
from django.test import TestCase
from ..models import Photo, Album
from django.contrib.auth.models import User
import factory


# Create your tests here.

# import pdb; pdb.set_trace()
#
#
#
#
# class AlbumTestCase(TestCase):
#
#     def setUp(self):
#         pass
#
#     # def setUp_user(self):
#     #     user = UserFactory.create()
#     #     user.save()
#
#     def tearDown(self):
#         pass
#
#     def test_upload_photo(self):
#         new_photo = PhotoFactory()
#         self.assertEqual(new_photo.upload, 'test_img.jpg')
#
#     def test_create_album_with_user(self):
#         new_album = Album()
#         self.user = UserFactory.create(username="sally")
