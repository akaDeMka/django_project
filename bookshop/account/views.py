from django.shortcuts import render
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
# Create your views here.
class MyLogin(LoginView):
    template_name='login.html'

class ChangeMyPassword(PasswordChangeView):
    template_name="change_password.html"
    success_url=reverse_lazy("account:change_password_done")

class ChangeMyPasswordDone(TemplateView):
    template_name="password_change_done.html"