from django import forms
from page.models import Page


class PageCreateForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ('name', 'slug', 'parent')