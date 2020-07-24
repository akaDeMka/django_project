from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from phonenumber_field.formfields import PhoneNumberField

class AccountCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class UserForm(forms.ModelForm):
    phone = PhoneNumberField()
    country=forms.CharField(max_length=30, required=False)
    city=forms.CharField(max_length=30, required=False)
    index=forms.CharField(max_length=15, required=False)
    address1=forms.CharField(max_length=150, required=False)
    address2=forms.CharField(max_length=150, required=False)
    notes = forms.CharField(widget=forms.Textarea, required=False) 
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'country', 'city', 'index', 'address1', 'address2', 'notes']