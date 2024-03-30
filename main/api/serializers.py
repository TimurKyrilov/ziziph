from rest_framework.serializers import ModelSerializer
from Content.models import Posts

class PostsThemeSerializer(ModelSerializer): 
    class Meta:
        model = Posts
        fields = ('user', 'theme')