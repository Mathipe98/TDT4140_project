"""
    Tests the functionality of the different views found in contact/views.py

    Functions:
        create_user(user_nr): Users
            Helper method for creating a user
        create_thread(user1, user2): Thread
            Helper method for creating a thread
        create_message(thread, sentto, sentfrom): Messages
            Helper method for creating a message

    Classes:
        SetUp(TestCase)
            Super class. Runs the setUp that is equal for most of the sub-classes.
        TestConversation(SetUp)
            Tests that the create_conversation method in views works as intended
        TestDetermineUsers(SetUp)
            Tests that the helper method determine_users_from_thread in views works as intended
        TestViewThread(SetUp)
            Tests that the view_threads method in views works as intended

"""

from django.test import TestCase, Client
from django.urls import reverse

from contact.models import Thread, Messages
from contact.views import determine_users_from_thread_id
from users.models import Users


def create_user(user_nr):
    """
    Creates a user with the specified number in the username. Returns Users object

    :param user_nr: int . The # of the user's name.
    :return Users object
    """
    return Users.objects.create(username="Test" + str(user_nr), password="tester1234", email="test@test.com",
                                firstname="Test", lastname="Test", admin=0, blocked=0)


def create_thread(user1, user2):
    """
    Creates a thread between two specified users. Returns Thread object

    :param user1: int. The primary key of the first user
    :param user2: int. The primary key of the second user.
    :return Thread object
    """
    return Thread.objects.create(user1_id=user1, user2_id=user2)


def create_message(thread, sent_to, sent_from):
    """
    Creates a message between two specified users. Returns Messages object

    :param thread: Thread. The Thread object between the two users
    :param sent_to: int. The primary key of the receiving user
    :param sent_from: int. The primary key of the sending user
    :return Messages object
    """
    return Messages.objects.create(thread_id=thread.pk, sentto=sent_to, sentfrom=sent_from)


class SetUp(TestCase):
    """
    Super class for the other test classes. Subclass of TestCase. Runs setUp that is equal for most of the sub-classes.

    Functions
        setUp: None
            Runs setup that occurs before each test

    Attributes
        PASSWORD: string
            common password used for all created users
        user1: Users
            first user in each test
        user2: Users
            second user in each test
        client: Client
            the client used to request views
    """
    PASSWORD = "tester1234"

    def setUp(self):
        """Sets up for each test"""
        self.user1 = create_user(1)
        self.user1.set_password(self.PASSWORD)  # Must be set through method, if not it will save it as a generated hash
        self.user1.save()  # Saves the updated model

        self.user2 = create_user(2)
        self.user2.set_password(self.PASSWORD)  # Must be set through method, if not it will save it as a generated hash
        self.user2.save()  # Saves the updated model

        self.client = Client()
        self.client.login(username=self.user1.username, password=self.PASSWORD)


class TestConversation(SetUp):
    """
    Subclass of SetUp. Tests that the create_conversation method in views works as intended

    Functions
        setUp: None
            Runs setup that occurs before each test
        test_create_conversation: None
            Tests creation of conversations via views
        test_create_convo_with_yourself: None
            Tests whether you can create a convo with yourself
        test_create_convo_with_nonexistant_user: None
            Tests whether you can create a convo with someone who does not exist
        test_create_convo_not_logged_in: None
            Tests whether you can create a convo when you are not logged in

    """

    def setUp(self):
        """Runs setup that occurs before each test. Returns None."""
        super().setUp()

    def test_create_conversation(self):
        """Tests creation of conversations via views. Returns None."""
        url = reverse("contact_user", args=[self.user2.pk])  # Requests the url of contact_user with pk = user2.pk
        self.assertEqual(url, '/messages/contact/2/')
        response_redirect = self.client.get(url, follow=False)
        # Follow = false means it won't be redirected immediately
        self.assertEqual(response_redirect.url, '/messages/messages/1')
        self.assertEqual(response_redirect.status_code, 302)
        response = self.client.get(response_redirect.url)  # Follows the redirect url now
        self.assertEqual(response.status_code, 200)

    def test_create_convo_with_yourself(self):
        """Tests whether you can create a convo with yourself. Returns None."""
        url = reverse("contact_user", args=[self.user1.pk])  # Tries to contact himself
        response_redirect = self.client.get(url, follow=False)
        self.assertEqual(response_redirect.url, '/')  # The home page url

    def test_create_convo_with_nonexistant_user(self):
        """Tests whether you can create a convo with someone who does not exist. Returns None."""
        url = reverse("contact_user", args=[3])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_create_convo_not_logged_in(self):
        """Tests whether you can create a convo when you are not logged in. Returns None."""
        self.client.logout()
        url = reverse("contact_user", args=[self.user1.pk])
        response = self.client.get(url)
        self.assertEqual(response.url, '/')


class TestDetermineUsers(SetUp):
    """
    Tests that the helper method determine_users_from_thread in views works as intended

    Functions
        setUp: None
            Runs setup that occurs before each test
        test_valid: None
            Tests whether the function works as intended with valid input
        test_user_not_in_thread: None
            Tests whether the function acts correctly when given a user who's not in the given thread

    Attributes
        thread: Thread
            A thread between user1 and user2
    """

    def setUp(self):
        """Runs setup that occurs before each test. Returns None."""
        super().setUp()
        self.thread = create_thread(self.user1.pk, self.user2.pk)

    def test_valid(self):
        """Tests whether the function works as intended with valid input. Returns None."""
        result_user_from, result_user_to, result_thread = determine_users_from_thread_id(self.user1, 1)
        self.assertEqual(result_user_from, self.user1)
        self.assertEqual(result_user_to, self.user2)
        self.assertEqual(result_thread.pk, self.thread.pk)

    def test_user_not_in_thread(self):
        """Tests whether the function acts correctly when given a user who's not in the given thread. Returns None."""
        user3 = Users.objects.create(username="Test3", password="tester1234", email="test@test.com",
                                     firstname="Test", lastname="Test", admin=0, blocked=0)
        result_user_from, result_user_to, result_thread = determine_users_from_thread_id(user3, 1)
        self.assertEqual(result_user_from, None)


class TestViewThread(SetUp):
    """
    Tests that the thread_view view functions as intended

    Functions
        setUp: None
            Runs setup that occurs before each test
        test_logged_out: None
            Tests that the user cannot view a thread when logged out, and is redirected to home
        test_no_threads_latest: None
            Tests that a user who is not part of any threads should be given an error page
        test_nonexistant_thread_request: None
            Tests that requesting a nonexistant thread yields and error page
        test_valid_thread: None
            Tests that creating a thread with valid information works


    Attributes
        user3: Users
            A third user
        thread1: Thread
            A thread between user1 and user2
        url: string
            The reversed url for view-threads
    """

    def setUp(self):
        """Runs setup that occurs before each test. Returns None."""
        super().setUp()
        self.user3 = create_user(3)
        self.thread1 = create_thread(self.user1.pk, self.user2.pk)
        self.url = reverse('view-threads')

    def test_logged_out(self):
        """Tests that the user cannot view a thread when logged out. Returns None"""
        self.client.logout()
        response = self.client.get(self.url, follow=False)  # Follow = false means it won't be redirected immediately
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        # Redirect to home page

    def test_no_threads_latest(self):
        """Tests that a user who is not part of any threads should be given an error page. Returns None"""
        self.user100 = create_user(100)
        self.client.get(self.url, follow=False)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        # Should return 200 OK but with different content than a valid thread
        self.assertIn('You have not created any conversations yet', str(response.content))

    def test_nonexistant_thread_request(self):
        """Tests that requesting a nonexistant thread yields and error page. Returns None"""
        url = reverse('view-threads', args=[2])  # Sends in 2 as a url argument to the view-threads url
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Should return 200 OK but with different content than a valid thread
        self.assertIn('There is no thread with this ID currently existing. Create a convo first', str(response.content))

    def test_valid_thread(self):
        """Tests that creating a thread with valid information works. Returns None"""
        self.msg = create_message(self.thread1, self.user1, self.user2)
        response = self.client.get(self.url)  # Should not redirect anywhere else
        self.assertEqual(response.status_code, 200)
        self.assertIn('Your conversation with', str(response.content))
