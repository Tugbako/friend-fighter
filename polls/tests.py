from django.test import TestCase, RequestFactory
from . import views

class HomeTest(TestCase):
  def test_index_view_should_get_OK(self):
    response = self.client.get('/hello')
    self.assertEqual(response.status_code, 200)

  def test_index_view_should_get_Hello_World(self):
    response = self.client.get('/hello')
    content = response.content
    self.assertEqual(content, b'Hello World')