from django.test import TestCase
from contact.models import Thread, Messages
from users.models import Users


class ThreadTestCase(TestCase):

    def setUp(self):
        self.user1 = Users.objects.create(username="Test", password="tester1234", email="test@test.com", firstname="Test", lastname="Test", admin=0, blocked=0)
        self.user2 = Users.objects.create(username="Test2", password="tester1234", email="test2@test.com",
                                          firstname="Test2", lastname="Test2", admin=0, blocked=0)
        self.thread = Thread.objects.create(user1=self.user1, user2=self.user2)

    def test_get_threadid(self):
        self.assertGreater(Thread.get_threadid(self.thread), 0)


class MessageTestCase(TestCase):

    def setUp(self):
        Messages.objects.create(
            message="Whats up",
            sent="2020-03-16 00:00:00",
            thread=1,
            sentto=2,
            sentfrom=1
        )
