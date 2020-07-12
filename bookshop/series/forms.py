from django import forms
from .models import Series

class CreateSeriesForm (forms.ModelForm):
    class Meta:
        model = Series
        fields = (
            'name',
        )
        # Не актуально при наличии crispy
        #widgets = {
        #    'name' : forms.TextInput(attrs={'class' : 'form-control'}),
        #    'description' : forms.Textarea(attrs={'class' : 'form-control'}),
        #}