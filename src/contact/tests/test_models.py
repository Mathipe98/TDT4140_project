"""
    Tests that the models in contact function as intended.

    Classes
        ThreadTestCase: TestCase
            Tests that the Thread model found in contact/models.py work as intended together with the associated models.
    
"""

from django.test import TestCase
from contact.models import Thread, Messages
from users.models import Users
from django.utils import timezone


class ThreadTestCase(TestCase):
    """
    Class testing that the Thread model found in contact/models.py work as intended together with the associated models.

    Functions
        setUp(self) : None
            Set up that occurs before each test
        test_get_thread_id(self): None
            Tests that the thread id is not 0 or negative
        test_publish(self): None
            Tests that the publish method in Messages works as intended
    """

    def setUp(self):
        """Creates a setup for which all the tests use. Returns None"""
        self.user1 = Users.objects.create(username="Test", password="tester1234", email="test@test.com",
                                          firstname="Test", lastname="Test", admin=0, blocked=0)
        self.user2 = Users.objects.create(username="Test2", password="tester1234", email="test2@test.com",
                                          firstname="Test2", lastname="Test2", admin=0, blocked=0)
        self.thread = Thread.objects.create(user1=self.user1, user2=self.user2)
        self.message = Messages.objects.create(
            message="Whats up",
            thread=self.thread,
            sentto=self.user2,
            sentfrom=self.user1
        )

    def test_get_threadid(self):
        """Tests that the thread id cannot be 0 or negative. Returns None"""
        self.assertGreater(self.thread.get_threadid(), 0)

    def test_publish(self):  # TODO: Move to another class?
        """Tests the publish method found in Messages. Returns None"""
        self.message.publish()
        self.assertGreater(self.message.sent.microsecond, timezone.now().microsecond - 2000)  # Takes some mS to execute



