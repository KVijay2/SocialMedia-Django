from django.test import TestCase
from .models import Tweet, Profile

class URLTests(TestCase):
  
  def test_homepage(self):
    response = self.client.get("/")
    self.assertEqual(response.status_code,200)

class ModelTests(TestCase):
  
  def profile_test_str(self):
    user = Profile.objects.create(user="vijaykarunanidhi@gmail.com")
    self.assertEqual(str(user),"vijaykarunanidhi@gmail.com")