from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.views.generic import TemplateView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Profile
from django.contrib.auth.models import User
from .forms import AccountCreationForm, UserForm, ProfileForm
from .signals import create_profile

# Create your views here.
#User=get_user_model()
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
    success_url = reverse_lazy("main:main")
    form_class = UserForm

    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super(EditAccount, self).get_context_data(**kwargs)
        user=self.request.user

        context.update({'form': UserForm(initial={
                'first_name':user.first_name,
                'last_name':user.last_name,
                'email':user.email,
                'phone':user.profile.phone,
                'country':user.profile.country,
                'city':user.profile.city,
                'index':user.profile.index,
                'address1':user.profile.address1,
                'address2':user.profile.address2,
                'notes':user.profile.notes,
            }),
        })
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        # Cleaned(normalized) data + Update Profile
        user.profile.phone = form.cleaned_data['phone']
        user.profile.country = form.cleaned_data['country']
        user.profile.city = form.cleaned_data['city']
        user.profile.index = form.cleaned_data['index']
        user.profile.address1 = form.cleaned_data['address1']
        user.profile.address2 = form.cleaned_data['address2']
        user.profile.notes = form.cleaned_data['notes']
        user.profile.save() 
 
        return super(EditAccount, self).form_valid(form)


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


