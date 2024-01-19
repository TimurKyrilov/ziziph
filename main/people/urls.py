from django.urls import path
from . import views as people_views

app_name = 'people'

urlpatterns = [
    path('<str:username>/', people_views.profile, name='profile'),
    path('<str:username>/edit/', people_views.edit_profile, name='edit_profile'),
]
