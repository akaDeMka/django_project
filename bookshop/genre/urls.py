from django.urls import path

from . import views

app_name = 'genre'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:genre_id>/create/',views.add,name='Add Genre'),
    path('<int:genre_id>/',views.edit,name="Edit Genre"),
    path('<int:genre_id>/delete/',views.delete,name="Delete Genre")
]