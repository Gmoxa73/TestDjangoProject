from django.test import TestCase
from rest_framework.test import APIClient

class MyTest(TestCase):
    def test_ok(self):
        self.assertTrue(True, True)

    def test_fail(self):
        url = "/"
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)