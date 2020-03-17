from django.test import TestCase
from contact.models import Thread, Messages
from users.models import Users
from django.utils import timezone


class ThreadTestCase(TestCase):

    def setUp(self):
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
        self.assertGreater(self.thread.get_threadid(), 0)

    def test_publish(self):
        self.message.publish()
        self.assertGreater(self.message.sent.microsecond, timezone.now().microsecond - 2000)  # Takes some mS to execute



