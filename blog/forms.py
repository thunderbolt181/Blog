from django import forms
from django.contrib.auth.models import User
from django.db import models
from blog.models import Post
from django.utils import timezone

class BlogCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','content','image']

class BlogUpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','content',"image"]