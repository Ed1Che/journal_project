from django import forms
from .models import Entry
from django import forms
from django.contrib.auth.models import User  # Django's built-in User model

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'content']
