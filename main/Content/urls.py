from django.urls import path
from Content import views as content_views
app_name = 'Content'

urlpatterns = [
    path('home/', content_views.main_page, name='home'),
]
