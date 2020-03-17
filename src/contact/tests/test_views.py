from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from contact.models import Thread
from contact.views import create_conversation, thread_view
from users.models import Users


class TestConversation(TestCase):

    def setUp(self):
        self.user1 = Users.objects.create(username="Test", password="tester1234", email="test@test.com",
                                          firstname="Test", lastname="Test", admin=0, blocked=0)
        self.user2 = Users.objects.create(username="Test2", password="tester1234", email="test2@test.com",
                                          firstname="Test2", lastname="Test2", admin=0, blocked=0)
        self.thread = Thread.objects.create(user1=self.user1, user2=self.user2)
        self.client = Client()

    def test_create_conversation(self):
        url = reverse("contact_user", args=[self.user2.pk])
        self.assertEqual(url, '/messages/contact/2/')
        request = self.client.get('/login/')
        request.user = self.user1
        response = create_conversation(request, self.user2.pk)
        self.assertEqual(response.status_code, 302)



