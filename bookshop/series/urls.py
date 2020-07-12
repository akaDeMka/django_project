from django.urls import path

from . import views

app_name = 'series'

urlpatterns = [
    path('', views.ViewSeries.as_view(), name="list"),
    path('create/',views.CreateSeries.as_view(),name="create"),
    path('<int:pk>/',views.DetailSeries.as_view(),name="detail"),
    path('<int:pk>/edit',views.EditSeries.as_view(),name="edit"),
    path('<int:pk>-delete/',views.DeleteSeries.as_view(),name="delete")
]