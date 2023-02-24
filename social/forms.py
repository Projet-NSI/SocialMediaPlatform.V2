from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    contenu = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Dites quelque chose...'
            }))

    class Meta:
        model = Post
        fields = ['contenu']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'rows': '3',
                   'placeholder': 'Dites quelque chose...'}
        ))

    class Meta:
        model = Comment
        fields = ['comment']  