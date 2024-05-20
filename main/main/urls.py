from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from api.views import PostsThemeViewApi

handler404 = 'Content.views.page_404'

router = DefaultRouter()
router.register('title', PostsThemeViewApi)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('profile/', include('people.urls', namespace='people')),
    path('', include('Content.urls', namespace='content')),
    path('api/', include(router.urls))
]

 