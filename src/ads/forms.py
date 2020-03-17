from django import forms
from .models import Advertisement, Category
from dal import autocomplete
from django_select2.forms import Select2MultipleWidget


class AdvertisementForm(forms.ModelForm):

    category = forms.ModelMultipleChoiceField(
        Category.objects.all().order_by('name'),
        label="Categories",
    )

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

