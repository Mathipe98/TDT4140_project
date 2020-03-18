from django import forms
from .models import Advertisement
from dal import autocomplete


class AdvertisementForm(forms.ModelForm):

    class Meta:
        model = Advertisement
        fields = ('product_name', 'product_description', 'price', 'header_picture', 'category')

    widgets = {
        'category': autocomplete.ModelSelect2Multiple(
            url='search:tag-autocomplete',
            attrs={'data-width': '100%'}
        )
    }



class ImageUploadForm(forms.Form):
    image = forms.ImageField(initial="default.png")

