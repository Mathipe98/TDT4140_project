from django import forms
from .models import Advertisement

class Advertisment_form(forms.ModelForm):

    class Meta:
        model = Advertisement
        fields = ('item', 'text','pris', 'image', 'published_date')

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

