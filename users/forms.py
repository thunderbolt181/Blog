from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile
from django.db import models

class registraionform(UserCreationForm):
    email=forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name' ,'password1', 'password2']

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['dob', 'address','image']
