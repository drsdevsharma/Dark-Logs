from django import forms
from .models import Post


class PostForm (forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title' , 'blog']
        labels = {'title': 'Title','blog':'Blog'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),'blog':forms.Textarea(attrs={'class':'form-control'})}