from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy
from .forms import CreateAuthorForm
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Author
class CreateAuthor(PermissionRequiredMixin,CreateView):
    permission_required = 'author.add_author'
    template_name = 'author_edit.html'
    model = Author
    form_class = CreateAuthorForm
    success_url = reverse_lazy("author:list")
class ViewAuthors(PermissionRequiredMixin, ListView):
    permission_required = 'author.view_author'
    template_name = 'author_list.html'
    model = Author
    paginate_by = 100
class EditAuthor(PermissionRequiredMixin,UpdateView):
    permission_required = 'author.change_author'
    template_name = 'author_edit.html'
    model = Author
    success_url = reverse_lazy("author:list")
    form_class = CreateAuthorForm
class DeleteAuthor(PermissionRequiredMixin,DeleteView):
    permission_required = 'author.delete_author'
    success_url = reverse_lazy("author:list")
    model = Author
    template_name = 'author_delete.html'
class DetailAuthor(PermissionRequiredMixin,DetailView):
    permission_required = 'author.view_author'
    template_name = 'author_detail.html'
    model = Author
    success_url = reverse_lazy("author:list")
    form_class = CreateAuthorForm

# Create your views here.
