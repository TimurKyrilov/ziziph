from django.urls import path
from .views import RegistrationView

app_name = 'Users'

urlpatterns = [
    # Другие шаблоны URL могут быть присутствовать
    path('signup/', RegistrationView.as_view(), name='signup'),
]
