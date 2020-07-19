from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from .forms import CreateBookForm
from .models import Book
class CreateBook(PermissionRequiredMixin, CreateView):
    permission_required = 'book.add_book'
    template_name = 'book_edit.html'
    model = Book
    form_class = CreateBookForm
    success_url = reverse_lazy("book:list")
class ViewBooks(PermissionRequiredMixin, ListView):
    permission_required = 'book.view_book'
    template_name = 'book_list.html'
    model = Book
    paginate_by = 30
class EditBook(PermissionRequiredMixin, UpdateView):
    permission_required = 'book.change_book'
    template_name = 'book_edit.html'
    model = Book
    success_url = reverse_lazy("book:list")
    form_class = CreateBookForm
class DeleteBook(PermissionRequiredMixin, DeleteView):
    permission_required = 'book.delete_book'
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