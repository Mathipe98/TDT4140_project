from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from users.models import Users
from ..models import Thread, Messages


class TestConversation(TestCase):

    def setUp(self):
        self.user1 = Users.objects.create(username="Test", password="tester1234", email="test@test.com",
                                          firstname="Test", lastname="Test", admin=0, blocked=0)
        self.user1.set_password("tester1234")  # Must be set through method, if not it will save it as a generated hash
        self.user1.save()

        self.user2 = Users.objects.create(username="Test2", password="tester1234", email="test2@test.com",
                                          firstname="Test2", lastname="Test2", admin=0, blocked=0)
        self.user2.set_password("tester1234")  # Must be set through method, if not it will save it as a generated hash
        self.user2.save()
        self.client = Client()

        self.client.login(username=self.user1.username, password="tester1234")
        self.client = Client()

    def test_create_convo(self):
        url = reverse("contact_user", args=[2])
        response_redirect = self.client.get(url, follow=False)
        self.assertEqual(response_redirect.url, '/messages/messages/1')
        response = self.client.get(response_redirect)
        self.assertEqual(response.status_code, 200)

    def test_create_convo_with_yourself(self):
        url = reverse("contact_user", args=[1])  # Tries to contact himself
        response_redirect = self.client.get(url, follow=False)
        self.assertEqual(response_redirect.url, '/')  # The home page url

    def test_create_convo_with_nonexistant_user(self):
        url = reverse("contact_user", args=[3])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_create_convo_not_logged_in(self):
        self.client.logout()
        url = reverse("contact_user", args=[1])
        response = self.client.get(url)
        self.assertEqual(response.url, '/')


class TestMessages(TestCase):

    def setUp(self):
        self.user1 = Users.objects.create(username="Test", password="tester1234", email="test@test.com",
                                          firstname="Test", lastname="Test", admin=0, blocked=0)
        self.user1.set_password("tester1234")  # Must be set through method, if not it will save it as a generated hash
        self.user1.save()

        self.user2 = Users.objects.create(username="Test2", password="tester1234", email="test2@test.com",
                                          firstname="Test2", lastname="Test2", admin=0, blocked=0)
        self.user2.set_password("tester1234")  # Must be set through method, if not it will save it as a generated hash
        self.user2.save()
        self.client = Client()

        self.client.login(username=self.user1.username, password="tester1234")
        self.thread = Thread.objects.create(user1_id=self.user1.userid, user2_id=self.user2.userid)

    
