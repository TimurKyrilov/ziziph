from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class RegistrationView(CreateView):
    template_name = "users/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('main')
