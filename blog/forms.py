from django import forms
from .models import Post
from django.views.generic import UpdateView


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

