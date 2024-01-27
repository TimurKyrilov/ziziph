from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    GENDER_CHOICES = [
        ('M', 'М'),
        ('Ж', 'Ж'),
    ]
    Belie_Chorniy = [
        ("Ч", "Ч"),
        ("Б", "Б"),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    Beli_ili_chorniy = models.CharField(max_length=1, choices=Belie_Chorniy, blank=True, null=True)

    def __str__(self):
        return self.user.username
