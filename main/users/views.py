from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class RegistrationView(CreateView):
    template_name = "users/signup.html"
    form_class = CustomUserCreationForm
    success_url = '/auth/profile/<str:username>/'

def logout_view(request):
    logout(request)
    return redirect('/') 