from . import views as users_views
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from .views import RegistrationView

app_name = 'Users'

urlpatterns = [
    path('signup/', RegistrationView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', users_views.logout_view, name='logout'),
]
