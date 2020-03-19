from django.test import SimpleTestCase
from ads.forms import AdvertisementForm


class TestForms(SimpleTestCase):
    """This class tests the input fields in the form that is used when creating or editing a new ad."""

    def test_ads_form_valid_data(self):
        form = AdvertisementForm(data={
            'product_name': 'Car',
            'product_description': 'I want to sell my Chevrolet 1980 model',
            'price': 1000000
        })

        self.assertTrue(form.is_valid())

    def test_ads_form_negative_price(self):
        form = AdvertisementForm(data={
            'product_name': 'Car',
            'product_description': 'I want to sell my Chevrolet 1980 model',
            'price': -1000
        })

        self.assertFalse(form.is_valid())

    def test_ads_form_no_price(self):
        form = AdvertisementForm(data={
            'product_name': 'Car',
            'product_description': 'I want to sell my Chevrolet 1980 model',
        })

        self.assertFalse(form.is_valid())

    def test_ads_form_no_product_name(self):
        form = AdvertisementForm(data={
            'product_description': 'I want to sell my Chevrolet 1980 model',
            'price': 10
        })

        self.assertFalse(form.is_valid())

    def test_ads_form_no_product_description(self):
        form = AdvertisementForm(data={
            'product_name': 'Car',
            'price': 10
        })

        self.assertFalse(form.is_valid())

    def test_ads_all_inputs_missing(self):
        form = AdvertisementForm(data={
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)      # checks that all 4 errors occurred for missing fields
