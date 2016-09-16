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

# Create your tests here.


# class ProfileTest(TestCase):

#     def create_profile(self, user="Fred"): 
#         User.objects.create(user=user)


#     def test_imager_profile_creation(self):
#         img_pro = self.create_profile()
#         self.assertTrue(isinstance(img_pro, ImagerProfile))



class AddressTest(TestCase):

    def create_address(self, street_addr="123 Address", city="ThisCity", state="WA", post_code="12345"): 
        id = a230e828-0149-4fa5-b53e-4807d22a9e9a

        Address.objects.create(imager_profile_id=id, street_addr=street_addr, city=city, state=state, post_code=post_code)


    def test_address_creation(self):
        this_addr = self.create_address()
        self.assertTrue(isinstance(this_addr, Address))


