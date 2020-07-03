from django.urls import path

from . import views

app_name = 'genre'

urlpatterns = [
    path('', views.ViewGenres.as_view(), name="list"),
    path('create/',views.CreateGenre.as_view(),name="create"),
    path('<int:pk>/',views.DetailGenre.as_view(),name="detail"),
    path('<int:pk>/edit',views.EditGenre.as_view(),name="edit"),
    path('<int:pk>-delete/',views.DeleteGenre.as_view(),name="delete")
]