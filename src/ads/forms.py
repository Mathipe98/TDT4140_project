"""
    Form for creating/changing the Advertisement model

    classes:
        AdvertisementForm : Form which allows you to create/change the product_name, product_description, price,
        header_picture and category of an Advertisement.
"""

from django import forms
from .models import Advertisement
from django.core.validators import MinValueValidator
from django.core import validators


class AdvertisementForm(forms.ModelForm):
    """
        Form for creating/editing an advertisement
    """

    class Meta:
        """
            Meta class for the advertisement form

            Attributes
                model : Model
                    Advertisement model
                fields : Tuple
                    The fields to change in the advertisement model
                widgets : Dictionary
                    Placeholders for the form fields
        """
        model = Advertisement
        fields = ('product_name', 'product_description', 'price', 'header_picture', 'category')

        # These widgets make placeholders (text that disappear when writing) in the input fields
        widgets = {
            'product_name': forms.Textarea(attrs={'placeholder': 'What is your product called?', 'required': True}),
            'product_description': forms.Textarea(attrs={'placeholder': 'Describe your product', 'required': True})
        }
