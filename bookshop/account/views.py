from django.shortcuts import render
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.views.generic import TemplateView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from .forms import AccountCreationForm
# Create your views here.
class MyLogin(LoginView):
    template_name='login.html'

class ChangeMyPassword(LoginRequiredMixin,PasswordChangeView):
    template_name="password_change.html"
    success_url=reverse_lazy("account:change_password_done")

class ChangeMyPasswordDone(TemplateView):
    template_name="password_change_done.html"

class LogOutMe (LoginRequiredMixin,LogoutView):
    template_name="logout.html"

class EditAccount(LoginRequiredMixin,UpdateView):
    template_name = 'account_update.html'
    model = User
    success_url = reverse_lazy("main:main")
    fields = ["username", "email","first_name","last_name"]

    def get_object(self):
        return self.request.user

class CreateNewAccount(CreateView):
    model=User
    form_class=AccountCreationForm
    template_name = 'account_create.html'
    success_url = reverse_lazy("account:login")

class MyPasswordReset(PasswordResetView):
    template_name = 'password_reset.html'
    success_url = reverse_lazy("account:password_reset_done")
    email_template_name = "password_reset_email.html"

class MyPasswordResetDone(PasswordResetDoneView):
    template_name = 'password_reset_done.html'
    success_url = reverse_lazy("account:login")

class MyPasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy("account:password_reset_complite")

class MyPasswordResetComplite(PasswordResetCompleteView):
    template_name='password_reset_complite.html'


