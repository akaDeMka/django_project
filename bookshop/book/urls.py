
from django.urls import path
from . import views

app_name = 'genre'

urlpatterns = [
    path('', views.ViewBooks.as_view(), name="list"),
    path('create/',views.CreateBook.as_view(),name="create"),
    path('<int:pk>/',views.DetailBook.as_view(),name="detail"),
    path('<int:pk>/edit',views.EditBook.as_view(),name="edit"),
    path('<int:pk>-delete/',views.DeleteBook.as_view(),name="delete")
]