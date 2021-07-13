from django.http import response
from snacks.models import Snack
from django.test import TestCase
from django.urls.base import reverse_lazy
from django.views.generic.base import View
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.

class viewTest(TestCase):
    def test_status_code(self):
        expected = 200
        actual = self.client.get(reverse('view')).status_code
        self.assertEqual(expected,actual)


