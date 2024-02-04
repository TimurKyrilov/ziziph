# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Posts(models.Model):
    author = models.CharField(max_length=20)
    theme = models.CharField(max_length=20)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.user.username
