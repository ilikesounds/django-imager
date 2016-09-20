from __future__ import unicode_literals

from django.test import TestCase
from .models import ImagerProfile, Address, Social, CameraType
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.dispatch import receiver
from django.db.models.signals import post_save
import uuid
from django.utils.translation import ugettext as _

import factory


# Create your tests here.

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user{}".format(n))
    email = factory.LazyAttribute(lambda x: "{}@example.com".format(x.username))


class ProfileTestCase(TestCase):

    def setUp(self):
        pass

    def setUp_five_users(self):
        self.users = []
        for i in range(5):
            user = UserFactory.create()
            user.save()
            self.users.append(user)


    def tearDown(self):
        pass


    def test_user_set_up_name(self):
        self.user = UserFactory.create(username="sally")
        self.assertEqual(self.user.username, 'sally')


    def test_profile_is_created_when_user_is_saved(self):
        self.setUp_five_users()
        self.assertTrue(ImagerProfile.objects.count() == 5)


    def test_user_set_up_names(self):
        self.setUp_five_users()
        self.assertEqual(self.users[0].username[:4], 'user')


    def test_user_set_up_emails(self):
        self.setUp_five_users()
        self.assertEqual(self.users[0].email[:4], 'user')


    def test_profile_is_created_when_user_is_saved(self):
        self.assertTrue(ImagerProfile.objects.count() == 0)
        self.user = UserFactory.create(username="sally")
        self.user.save()
        self.assertTrue(ImagerProfile.objects.count() == 1)


    def test_profile_str_is_user_username(self):
        self.user = UserFactory.create(username="sally")
        self.user.save()
        profile = ImagerProfile.objects.get(user=self.user)
        self.assertEqual(str(profile), self.user.username)


    def test_profile_is_active_on_create(self):
        self.user = UserFactory.create(username="sally")
        self.user.save()
        profile = ImagerProfile.objects.get(user=self.user)
        self.assertTrue(profile.active)


class AddressTest(TestCase):
    def create_address(self, street_addr="123 Address", city="ThisCity", state="WA", post_code="12345"): 
        self.user = UserFactory.create(username="sally")
        this_addr = self.user.imagerprofile.address.create(street_addr=street_addr, city=city, state=state, post_code=post_code)
        # self.user.imagerprofile.address.add(this_addr)


    def test_address_creation(self):
        self.create_address()
        # give me the address attached to the profile that belongs to the user with this pk value
        this_addr = Address.objects.filter(imager_profile__user__pk = self.user.pk)[0]
        self.assertTrue(isinstance(this_addr, Address))


    def test_address_check_addr(self):
        self.create_address()
        this_addr = Address.objects.filter(imager_profile__user__pk = self.user.pk)[0]
        self.assertEqual(this_addr.street_addr, "123 Address")


    def test_address_check_city(self):
        self.create_address()
        this_addr = Address.objects.filter(imager_profile__user__pk = self.user.pk)[0]
        self.assertEqual(this_addr.city, "ThisCity")


    def test_address_check_state(self):
        self.create_address()
        this_addr = Address.objects.filter(imager_profile__user__pk = self.user.pk)[0]
        self.assertEqual(this_addr.state, "WA")


    def test_address_check_postal(self):
        self.create_address()
        this_addr = Address.objects.filter(imager_profile__user__pk = self.user.pk)[0]
        self.assertEqual(this_addr.post_code, "12345")


class SocialTest(TestCase):
    def create_social(self, social_type="twiter", social_url="@twiteruser"): 
        self.user = UserFactory.create(username="rosie")
        this_social = self.user.imagerprofile.social.create(social_type=social_type, social_url=social_url)
        self.user.imagerprofile.social.add(this_social)


    def test_social_creation(self):
        self.create_social()
        this_social = Social.objects.filter(imager_profile__user__pk = self.user.pk)[0]
        self.assertTrue(isinstance(this_social, Social))


class CameraTest(TestCase):
    def create_camera(self, camera_type="canon"): 
        self.user = UserFactory.create(username="elle")
        this_camera = self.user.imagerprofile.camera_type.create(camera_type=camera_type)
        self.user.imagerprofile.camera_type.add(this_camera)


    def test_camera_creation(self):
        self.create_camera()
        this_camera = CameraType.objects.filter(imager_profile__user__pk = self.user.pk)[0]
        self.assertTrue(isinstance(this_camera, CameraType))


