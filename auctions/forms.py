from django import forms

from auctions.models import Listing, Comment


class ListingModelForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)