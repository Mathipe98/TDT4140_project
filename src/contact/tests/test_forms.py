from django.test import TestCase
from contact.forms import MessageForm


class TestMessageForm(TestCase):

    def test_standard_message(self):
        data = {
            'message': "Whats up"
        }
        form = MessageForm(data=data)
        form.is_valid()
        self.assertFalse(form.errors)  # The form should not give an error

    def test_empty_message(self):
        data = {
            "message": ""
        }
        form = MessageForm(data=data)
        form.is_valid()
        self.assertTrue(form.errors)
