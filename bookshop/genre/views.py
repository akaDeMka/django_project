from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView

from .forms import CreateGenreForm
from .models import Genre

# Create your views here.
class CreateGenre(CreateView):
    template_name = 'edit_genre.html'
    model = Genre
    form_class = CreateGenreForm
    success_url = "/genre"
class ViewGenres(ListView):
    #template_name = 'index.html'
    model = Genre
    paginate_by = 100
class EditGenre(UpdateView):
    template_name = 'edit_genre.html'
    model = Genre
    success_url = "/genre"
    form_class = CreateGenreForm
class DeleteGenre(DeleteView):
    template_name = 'delete_genre.html'
    model = Genre
    form_class = CreateGenreForm
    success_url = "/genre"
