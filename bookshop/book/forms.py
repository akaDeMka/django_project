from django import forms
from .models import Book

class CreateBookForm (forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'name',
            'description',
            'price',
            'date_pub',
            'pages',
            'binding',
            'isbn',
            'weight',
            'age_rating'
       )