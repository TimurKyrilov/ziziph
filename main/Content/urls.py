from django.urls import path
from Content import views as content_views

app_name = 'Content'

urlpatterns = [
    path('home/', content_views.main_page, name='home'),
    path('', content_views.redirecting_page, name='redirect'),
    path('create/<str:username>/', content_views.PostsCreateView.as_view(), name='create_post'),
    path('post/<str:username>/<int:pk>/', content_views.PostsDetailView.as_view(), name='post_detail'),
    path('post/api/<str:username>/<int:pk>/', content_views.GetView.as_view(), name='get_api')
]
