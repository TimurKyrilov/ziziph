from Content import views as content_views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', content_views.main_page, name='main'),
]
