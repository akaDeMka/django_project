from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy
from .forms import CreateAuthorForm

from .models import Author
class CreateAuthor(CreateView):
    template_name = 'author_edit.html'
    model = Author
    form_class = CreateAuthorForm
    success_url = reverse_lazy("author:list")
class ViewAuthors(ListView):
    template_name = 'author_list.html'
    model = Author
    paginate_by = 100
class EditAuthor(UpdateView):
    template_name = 'author_edit.html'
    model = Author
    success_url = reverse_lazy("author:list")
    form_class = CreateAuthorForm
class DeleteAuthor(DeleteView):
    success_url = reverse_lazy("author:list")
    model = Author
    template_name = 'author_delete.html'
class DetailAuthor(DetailView):
    template_name = 'author_detail.html'
    model = Author
    success_url = reverse_lazy("author:list")
    form_class = CreateAuthorForm

# Create your views here.
