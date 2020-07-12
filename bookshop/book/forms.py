from django import forms
from .models import Book

class CreateBookForm (forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'name',
            'description',
            'image',
            'price',
            'authors',
            'series',
            'genres',
            'year',
            'pages',
            'binding',
            'format',
            'isbn',
            'weight',
            'age_rating',
            'publisher',
            'quantity',
            'active',
            'rating',
       )

#class ViewBookForm (forms.Form):
    