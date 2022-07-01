from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    GENDER = (('M', 'Male'), ('F', 'Female'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=10)
    gender = models.CharField(choices=GENDER, max_length=20)
    weight = models.FloatField("Weight in kg", default=40)
    height = models.FloatField("Height in cm", default=150)

    def __str__(self):
        return f"{self.user}"
