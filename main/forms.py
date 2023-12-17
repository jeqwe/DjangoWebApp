from django import forms
from main.models import News


class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'author', 'photo', 'teaser', 'text']

