from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout, login, authenticate
from accounts.forms import SignUpForm, CustomLoginForm, CustomPasswordResetForm, CustomPasswordResetConfirmForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView




class SignUpView(generic.CreateView):
    form_class = SignUpForm #We're subclassing the generic class-based view CreateView in our SignUp class. We specify using the built-in UserCreationForm
    success_url = reverse_lazy("home") #to redirect the user to the home page upon successful registration.
    template_name = "registration/signup.html"

    # To autologin after successful signup
    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return valid

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    redirect_authenticated_user: bool = True
    success_url = reverse_lazy("home")
    template_name: str = "registration/login.html"

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    # redirect_authenticated_user: bool = True
    success_url = reverse_lazy("password_reset_done")
    template_name: str = "registration/password_reset.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomPasswordResetConfirmForm
    success_url = reverse_lazy("password_reset_complete")
    template_name: str = "registration/password_reset_confirm.html"
        

def logout_view(request):
    logout(request)


# Create your views here.
