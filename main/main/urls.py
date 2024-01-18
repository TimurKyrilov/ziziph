from Content import views as content_views
from django.contrib import admin
from django.urls import path, include
from people import views as people_views

handler404 = 'Content.views.page_404'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', content_views.main_page, name='main'),
    path('auth/', include('users.urls', namespace='users')),
    path('', include('people.urls', namespace='people')),
]

