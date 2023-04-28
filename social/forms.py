from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    '''Défini les champs d'un formulaire, ici celui des posts'''
    contenu = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Dites quelque chose...'
            }))
    
    image = forms.ImageField(required=False)

    class Meta:
        '''Etabli le modèle du formulaire pour sauvegarder les champs dans la base de données'''
        model = Post
        fields = ['contenu','image']

class CommentForm(forms.ModelForm):
    '''Champs des commentaires'''
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'rows': '3',
                   'placeholder': 'Dites quelque chose...'}
        ))

    class Meta:
        '''Etabli le modèle du formulaire pour sauvegarder les champs dans la base de données'''
        model = Comment
        fields = ['comment']  