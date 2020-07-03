from django import forms
from .models import Genre

class CreateGenreForm (forms.ModelForm):
    class Meta:
        model = Genre
        fields = (
            'name',
            'description'
        )
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control'}),
        }