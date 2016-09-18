from __future__ import unicode_literals

from django.test import TestCase
from .models import ImagerProfile, Address
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
        # import pdb; pdb.set_trace()
        self.user.imagerprofile.address.create(street_addr=street_addr, city=city, state=state, post_code=post_code)


    def test_address_creation(self):
        this_addr = self.create_address()
        import pdb; pdb.set_trace()
        self.assertTrue(isinstance(this_addr, Address))




