from django.http import response
from django.test import TestCase

class EasyShoppingTest(TestCase):
    def test_home_view_exist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

def test_show_result_exist(self):
     response = self.client.get('search/')
     self.assertEqual(response.status_code, 200)

