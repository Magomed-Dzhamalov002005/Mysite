from django import forms
from .models import Post

class PostAddingForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput)
    
    class Meta:
        model = Post
        fields = ['slug', 'image', 'name', 'text', 'date']