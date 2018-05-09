from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post #tells Django which model should be considered
        fields = ('title', 'text',)
