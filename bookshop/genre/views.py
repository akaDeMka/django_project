from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import get_user_model

from .forms import CreateGenreForm
from .models import Genre
class CreateGenre(PermissionRequiredMixin,CreateView):
    permission_required = 'genre.add_genre'
    template_name = 'genre_edit.html'
    model = Genre
    form_class = CreateGenreForm
    success_url = reverse_lazy("genre:list")
class ViewGenres(PermissionRequiredMixin,ListView):
    permission_required = 'genre.view_genre'
    template_name = 'genre_list.html'
    model = Genre
    paginate_by = 100

class EditGenre(PermissionRequiredMixin,UpdateView):
    permission_required = 'genre.change_genre'
    template_name = 'genre_edit.html'
    model = Genre
    success_url = reverse_lazy("genre:list")
    form_class = CreateGenreForm
class DeleteGenre(PermissionRequiredMixin,DeleteView):
    permission_required = 'genre.delete_genre'
    success_url = reverse_lazy("genre:list")
    model = Genre
    template_name = 'genre_delete.html'
class DetailGenre(PermissionRequiredMixin,DetailView):
    permission_required = 'genre.view_genre'
    template_name = 'genre_detail.html'
    model = Genre
    success_url = reverse_lazy("genre:list")
    form_class = CreateGenreForm
    
