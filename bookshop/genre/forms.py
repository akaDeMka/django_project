from django import forms
from .models import Genre

class CreateGenreForm (forms.ModelForm):
    class Meta:
        model = Genre
        fields = (
            'name',
            'description'
        )
        # Не актуально при наличии crispy
        #widgets = {
        #    'name' : forms.TextInput(attrs={'class' : 'form-control'}),
        #    'description' : forms.Textarea(attrs={'class' : 'form-control'}),
        #}