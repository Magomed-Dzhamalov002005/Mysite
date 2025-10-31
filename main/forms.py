from django import forms
from .models import Post, Comment

class PostAddingForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput)
    
    class Meta:
        model = Post
        fields = ['slug', 'image', 'name', 'text']


class CommentForm(forms.ModelForm):
    text = forms.CharField(max_length=1000, widget=forms.Textarea)
    
    class Meta:
        model = Comment
        fields = ['text']