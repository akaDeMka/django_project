from django.urls import path

from . import views

app_name = 'author'

urlpatterns = [
    path('', views.ViewAuthors.as_view(), name="list"),
    path('create/',views.CreateAuthor.as_view(),name="create"),
    path('<int:pk>/',views.DetailAuthor.as_view(),name="detail"),
    path('<int:pk>/edit',views.EditAuthor.as_view(),name="edit"),
    path('<int:pk>-delete/',views.DeleteAuthor.as_view(),name="delete")
]