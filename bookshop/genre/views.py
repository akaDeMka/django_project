from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .forms import CreateGenreForm
from .models import Genre

# Create your views here.
class CreateGenre(CreateView):
    template_name = 'genre_edit.html'
    model = Genre
    form_class = CreateGenreForm
    success_url = "/genre"
class ViewGenres(ListView):
    template_name = 'genre_list.html'
    model = Genre
    paginate_by = 100
class EditGenre(UpdateView):
    template_name = 'genre_edit.html'
    model = Genre
    success_url = "/genre"
    form_class = CreateGenreForm
class DeleteGenre(DeleteView):
    success_url = "/genre"
    model = Genre
    template_name = 'genre_delete.html'
    
