from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from contact.models import Thread
from contact.views import create_conversation, thread_view, determine_users_from_thread_id, save_msg_form
from users.models import Users


def create_user(user_nr):
    return Users.objects.create(username="Test" + str(user_nr), password="tester1234", email="test@test.com",
                                firstname="Test", lastname="Test", admin=0, blocked=0)


def create_thread(user1, user2):
    return Thread.objects.create(user1_id=user1, user2_id=user2)


class SetUp(TestCase):
    PASSWORD = "tester1234"

    def setUp(self):
        self.user1 = create_user(1)
        self.user1.set_password(self.PASSWORD)  # Must be set through method, if not it will save it as a generated hash
        self.user1.save()

        self.user2 = create_user(2)
        self.user2.set_password(self.PASSWORD)  # Must be set through method, if not it will save it as a generated hash
        self.user2.save()
        self.client = Client()
        self.client.login(username=self.user1.username, password=self.PASSWORD)


class TestConversation(SetUp):

    def setUp(self):
        super().setUp()

    def test_create_conversation(self):
        url = reverse("contact_user", args=[self.user2.pk])
        self.assertEqual(url, '/messages/contact/2/')
        response_redirect = self.client.get(url, follow=False)
        self.assertEqual(response_redirect.url, '/messages/messages/1')
        self.assertEqual(response_redirect.status_code, 302)
        response = self.client.get(response_redirect.url)
        self.assertEqual(response.status_code, 200)

    def test_create_convo_with_yourself(self):
        url = reverse("contact_user", args=[self.user1.pk])  # Tries to contact himself
        response_redirect = self.client.get(url, follow=False)
        self.assertEqual(response_redirect.url, '/')  # The home page url

    def test_create_convo_with_nonexistant_user(self):
        url = reverse("contact_user", args=[3])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_create_convo_not_logged_in(self):
        self.client.logout()
        url = reverse("contact_user", args=[self.user1.pk])
        response = self.client.get(url)
        self.assertEqual(response.url, '/')


class TestMessages(SetUp):

    def setUp(self):
        super().setUp()
        self.thread = create_thread(self.user1.pk, self.user2.pk)


class TestDetermineUsers(SetUp):

    def setUp(self):
        super().setUp()
        self.thread = create_thread(self.user1.pk, self.user2.pk)

    def test_valid(self):
        result_user_from, result_user_to, result_thread = determine_users_from_thread_id(self.user1, 1)
        self.assertEqual(result_user_from, self.user1)
        self.assertEqual(result_user_to, self.user2)
        self.assertEqual(result_thread.pk, self.thread.pk)

    def test_user_not_in_thread(self):
        self.user3 = Users.objects.create(username="Test3", password="tester1234", email="test@test.com",
                                          firstname="Test", lastname="Test", admin=0, blocked=0)
        result_user_from, result_user_to, result_thread = determine_users_from_thread_id(self.user3, 1)
        self.assertEqual(result_user_from, None)


class TestViewThread(SetUp):

    def setUp(self):
        super().setUp()
        self.user3 = create_user(3)
        self.thread1 = create_thread(self.user1.pk, self.user2.pk)
        self.url = reverse('view-threads')

    def test_logged_out(self):
        self.client.logout()
        response = self.client.get(self.url, follow=False)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')

    def test_no_threads(self):
        self.user100 = create_user(100)
        self.client.get(self.url, follow=False)
        response = self.client.get(self.url, follow=False)
        self.assertEqual(response.status_code, 404)

    def test_nonexistant_thread(self):
        url = reverse('view-threads', args=[2])
        response = self.client.get(url, follow=False)
        self.assertEqual(response.status_code, 404)

    