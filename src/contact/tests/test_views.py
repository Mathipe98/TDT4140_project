from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from users.models import Users


class TestConversation(TestCase):

    def setUp(self):
        self.user1 = Users.objects.create(username="Test", password="tester1234", email="test@test.com",
                                          firstname="Test", lastname="Test", admin=0, blocked=0)
        self.user2 = Users.objects.create(username="Test2", password="tester1234", email="test2@test.com",
                                          firstname="Test2", lastname="Test2", admin=0, blocked=0)
        self.client = Client()

    def test_create_conversation(self):
        url = reverse("contact_user", args=[1])

        response = self.client.get(url)
        self.assertEqual(response.status, 200)
