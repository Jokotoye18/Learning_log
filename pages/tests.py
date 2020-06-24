from django.test import TestCase, SimpleTestCase
from django.urls import reverse


class HomepageTest(SimpleTestCase):

    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_by_url_name(self):
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200)


