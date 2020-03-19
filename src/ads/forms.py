from django import forms
from .models import Advertisement
from django.core.validators import MinValueValidator
from django.core import validators


class AdvertisementForm(forms.ModelForm):

    class Meta:
        model = Advertisement
        fields = ('product_name', 'product_description', 'price', 'header_picture', 'category')

        # These widgets make placeholders (text that disappear when writing) in the input fields
        widgets = {
            'product_name': forms.Textarea(attrs={'placeholder': 'What is your product called?', 'required': True}),
            'product_description': forms.Textarea(attrs={'placeholder': 'Describe your product', 'required': True})
        }


class ImageUploadForm(forms.Form):
    image = forms.ImageField(initial="default.png")

