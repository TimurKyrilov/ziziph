from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Posts(models.Model):
    theme = models.CharField(max_length=20)
    text = models.TextField()
    
    def __str__(self):
        return self.user.username