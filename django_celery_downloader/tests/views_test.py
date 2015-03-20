"""
    Test that 2 of 3 views are working properly

    A good faith effort: unit tests only, integration tests coming soon

    I can't test the async tasks unitl I get selenium integration tests running
"""

from django.test import TestCase
from django.test.client import Client


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_base_view(self):
        response = self.client.get('/report/')
        self.assertEqual(response.status_code, 200)

    def test_modal_view(self):
        response = self.client.get('/report/csv-modal/5/')
        self.assertEqual(response.status_code, 200)
