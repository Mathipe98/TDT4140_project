from django import forms
from .models import Thread
from .models import Messages


class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ["message"]

        widgets = {
            'message': forms.Textarea(attrs={'class': 'messageClass', 'rows': 1}),
        }

    def clean(self):
        message = self.cleaned_data.get('message')
        return self.cleaned_data
