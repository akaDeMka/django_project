from django.urls import path

from .views import CreateGenre, EditGenre, ViewGenres, DeleteGenre

app_name = 'genre'

urlpatterns = [
    path('', ViewGenres.as_view(), name='genre_list'),
    path('create/',CreateGenre.as_view(),name='Add Genre'),
    path('<int:pk>/',EditGenre.as_view(),name="Edit Genre"),
    path('<int:pk>/delete/',DeleteGenre.as_view(),name="Delete Genre")
]