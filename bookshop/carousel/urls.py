
from django.urls import path
from . import views

app_name = 'carousel'

urlpatterns = [
    path('', views.ViewCarousel.as_view(), name="carousel"),

]