from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=False, validators=[MaxValueValidator(100)])
    GENDER_CHOICES = [
        ('M', 'М'),
        ('F', 'Ж'),
    ]
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    def __str__(self):
        return self.user.username