from django.urls import path
from .views import RegistrationView
from django.contrib.auth.views import LoginView

app_name = 'Users'

urlpatterns = [
    path('signup/', RegistrationView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
]
