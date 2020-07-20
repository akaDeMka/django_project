from django.shortcuts import render
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.views.generic import TemplateView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from .forms import AccountCreationForm
# Create your views here.
class MyLogin(LoginView):
    template_name='login.html'

class ChangeMyPassword(LoginRequiredMixin,PasswordChangeView):
    template_name="change_password.html"
    success_url=reverse_lazy("account:change_password_done")

class ChangeMyPasswordDone(LoginRequiredMixin,TemplateView):
    template_name="password_change_done.html"

class LogOutMe (LoginRequiredMixin,LogoutView):
    template_name="logout.html"

class EditAccount(PermissionRequiredMixin,UpdateView):
    permission_required = 'update_user'
    template_name = 'account_update.html'
    model = User
    success_url = reverse_lazy("main:main")
    fields = ["username", "email","first_name","last_name"]

class CreateNewAccount(CreateView):
    model=User
    form_class=AccountCreationForm
    template_name = 'account_create.html'
    #success_url = reverse_lazy("account:update")