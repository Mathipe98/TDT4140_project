from django.test import TestCase
from contact.forms import MessageForm

class TestMessageForm(TestCase):

    def test_message_form(self):
        data = {
            'message': "Whats up"
        }
        form = MessageForm(data=data)
        form.is_valid()
        self.assertTrue(form.errors)