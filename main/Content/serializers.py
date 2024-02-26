from rest_framework import serializers
from .models import Posts

class PostsSerializers(models.ModelSerializer):
    class Meta:
        model = Posts
        field = "__all__"
    