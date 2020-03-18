from django import forms
from .models import Advertisement


class AdvertisementForm(forms.ModelForm):

    class Meta:
        model = Advertisement
        fields = ('product_name', 'product_description', 'price', 'header_picture', 'category')


class ImageUploadForm(forms.Form):
    image = forms.ImageField(initial="default.png")

