from django import forms
from .models import Book

class CreateBookForm (forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'name',
            'description',
            'price',
            'year',
            'pages',
            'binding',
            'isbn',
            'weight',
            'age_rating',
            'quantity',
            'active',
            'rating'
       )

#class ViewBookForm (forms.Form):
    