from django.urls import path

from . import views

app_name = 'publisher'

urlpatterns = [
    path('', views.ViewPublishers.as_view(), name="list"),
    path('create/',views.CreatePublisher.as_view(),name="create"),
    path('<int:pk>/',views.DetailPublisher.as_view(),name="detail"),
    path('<int:pk>/edit',views.EditPublisher.as_view(),name="edit"),
    path('<int:pk>-delete/',views.DeletePublisher.as_view(),name="delete")
]