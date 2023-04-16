from django import forms
from django.forms import ModelForm
from .models import Post,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User



class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['slug', 'writer']


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':'form-cotrol','placeholder':"Enter UserName"}))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={
        'class': 'form-cotrol', 'placeholder': "Enter your Email"}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-cotrol', 'placeholder': "Enter Password"}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-cotrol', 'placeholder': "Enter Confirm Password"}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CommentForm(forms.ModelForm):
    commenter = forms.CharField(max_length=20, widget = forms.TextInput(attrs={
         'class':'form-control','placeholder':'Your Name'
    }) )

    body = forms.CharField(max_length=100, widget=forms.Textarea(attrs={
        'class':'form-control','placeholder':'Comment here'
    }) )
    class Meta:
        model = Comment
        fields = ['commenter', 'body']