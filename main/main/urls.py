from Content import views as content_views
from django.contrib import admin
from django.urls import path, include
from people import views as people_views

handler404 = 'Content.views.page_404'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('profile/', include('people.urls', namespace='people')),
    path('', include('Content.urls', namespace='content'))
]

