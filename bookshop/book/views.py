from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy

from .forms import CreateBookForm
from .models import Book
class CreateBook(CreateView):
    template_name = 'book_edit.html'
    model = Book
    form_class = CreateBookForm
    success_url = reverse_lazy("book:list")
class ViewBooks(ListView):
    template_name = 'book_list.html'
    model = Book
    paginate_by = 100
class EditBook(UpdateView):
    template_name = 'book_edit.html'
    model = Book
    success_url = reverse_lazy("book:list")
    form_class = CreateBookForm
class DeleteBook(DeleteView):
    success_url = reverse_lazy("book:list")
    model = Book
    template_name = 'book_delete.html'
class DetailBook(DetailView):
    template_name = 'book_detail.html'
    model = Book
    success_url = reverse_lazy("book:list")
class CardBooks(ListView):
    template_name = 'book_cards.html'
    model = Book
    paginate_by = 10