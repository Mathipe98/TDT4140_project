""" Integration and unit testing module using Django test objects

    Classes:
        TestUsersAttributes
        TestAdvertisementAttributes
        TestStatisticsPageInput
"""

from django.db.models import BooleanField, DateTimeField
from django.test import TestCase

from ads.models import Advertisement
from stats.views import statistics_context
from users.models import Users


class TestUsersAttributes(TestCase):
    """ This class tests if the Users class has the correct attributes """

    def test_if_class_has_objects_attribute(self):
        self.assertTrue(hasattr(Users, 'objects'))

    def test_if_class_objects_has_all_method(self):
        self.assertTrue(callable(getattr(Users.objects, 'all', None)))

    def test_if_all_objects_has_count_method(self):
        self.assertTrue(callable(getattr(Users.objects.all(), 'count', None)))

    def test_if_count_returns_int(self):
        self.assertIsInstance(Users.objects.all().count(), int)


class TestAdvertisementAttributes(TestCase):
    """ This class tests if the Advertisement class has the correct attributes """

    def test_if_class_has_objects_attribute(self):
        self.assertTrue(hasattr(Advertisement, 'objects'))

    def test_if_class_objects_has_all_method(self):
        self.assertTrue(callable(getattr(Advertisement.objects, 'all', None)))

    def test_if_all_objects_has_count_method(self):
        self.assertTrue(callable(getattr(Advertisement.objects.all(), 'count', None)))

    def test_if_count_returns_int(self):
        self.assertIsInstance(Advertisement.objects.all().count(), int)

    def test_if_class_has_sold_attribute(self):
        self.assertTrue(hasattr(Advertisement, 'sold'))

    def test_if_sold_attribute_is_bool(self):
        self.assertIsInstance(Advertisement._meta.get_field('sold'), BooleanField)

    def test_if_class_has_sold_date_attribute(self):
        self.assertTrue(hasattr(Advertisement, 'sold_date'))

    def test_if_sold_date_attribute_is_datetime(self):
        self.assertIsInstance(Advertisement._meta.get_field('sold_date'), DateTimeField)

    def test_if_class_has_published_date_attribute(self):
        self.assertTrue(hasattr(Advertisement, 'published_date'))

    def test_if_published_date_attribute_is_datetime(self):
        self.assertIsInstance(Advertisement._meta.get_field('published_date'), DateTimeField)


class TestStatisticsPageInput(TestCase):
    """ This class tests the validity of the context input fields shown in the statistics page """

    def test_users_count_validity(self):
        self.assertIsInstance(statistics_context()['users_count'], int)

    def test_advertisement_count_validity(self):
        self.assertIsInstance(statistics_context()['advertisements_count'], int)

    def test_sold_items_count_validity(self):
        self.assertIsInstance(statistics_context()['sold_items_count'], int)

    def test_average_sell_time_validity(self):
        self.assertIsInstance(statistics_context()['average_sell_time'], str)
