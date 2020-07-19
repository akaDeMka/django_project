from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    #path('', views.ViewMain.as_view(), name="main"),
    path('login/', views.MyLogin.as_view(), name="login"),
    path('change_password/', views.ChangeMyPassword.as_view(), name="change_password"),
    path('change_password_done/', views.ChangeMyPasswordDone.as_view(),name="change_password_done"),
]