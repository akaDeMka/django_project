from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy

from .forms import CreateGenreForm
from .models import Genre
class CreateGenre(CreateView):
    template_name = 'genre_edit.html'
    model = Genre
    form_class = CreateGenreForm
    success_url = reverse_lazy("genre:list")
class ViewGenres(ListView):
    template_name = 'genre_list.html'
    model = Genre
    paginate_by = 100
class EditGenre(UpdateView):
    template_name = 'genre_edit.html'
    model = Genre
    success_url = reverse_lazy("genre:list")
    form_class = CreateGenreForm
class DeleteGenre(DeleteView):
    success_url = reverse_lazy("genre:list")
    model = Genre
    template_name = 'genre_delete.html'
class DetailGenre(DetailView):
    template_name = 'genre_detail.html'
    model = Genre
    success_url = reverse_lazy("genre:list")
    form_class = CreateGenreForm
    
