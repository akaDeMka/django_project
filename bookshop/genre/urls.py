from django.urls import path

from .views import CreateGenre, EditGenre, ViewGenres, DeleteGenre

app_name = 'genre'

urlpatterns = [
    path('', ViewGenres.as_view(), name="list"),
    path('create/',CreateGenre.as_view(),name="create"),
    path('<int:pk>/',EditGenre.as_view(),name="edit"),
    path('<int:pk>-delete/',DeleteGenre.as_view(),name="delete")
]