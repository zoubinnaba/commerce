from django import forms

from auctions.models import Listing


class ListingModelForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'