
from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from django import forms
from .views import searchView
from ads.forms import AdvertisementForm
from django.test.client import RequestFactory


class TestSearch(TestCase):
    """
    This class is testing the HTTP-response from the views. 200 OK if new HTML, or 302 if redirect. 400 is no response.
    It also assures that the templates are correct.
    """
    def setUp(self):
        """Make an advertisement in test db"""
        form = AdvertisementForm(data={
            'product_name': 'Car',
            'product_description': 'I want to sell my Chevrolet 1980 model',
            'price': 1000000
        })
        self.factory = RequestFactory()

    def test_search_result(self):
        """Try to search for Car advertisement, check for response"""
        request = self.factory.get('/results/?q=Car')
        response = searchView(request)
        self.assertEqual(response.status_code, 200)


