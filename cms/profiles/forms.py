from django import forms
from django.forms import ModelForm
from .models import UserProfiles


class UpdateProfileForm(ModelForm):
    class Meta:
        model = UserProfiles
        exclude = ['user']
