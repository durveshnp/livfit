from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    qty = models.CharField(max_length=120)
    unit = models.CharField(max_length=120)
    food = models.CharField(max_length=120)
    calories = models.CharField(max_length=120)
    weight = models.CharField(max_length=120)

    carbohydrates = models.CharField(max_length=120)
    fiber = models.CharField(max_length=120)
    sugar = models.CharField(max_length=120)
    fats = models.CharField(max_length=120)
    protein = models.CharField(max_length=120)

    phosphorus = models.CharField(max_length=120)
    potassium = models.CharField(max_length=120)
    energy = models.CharField(max_length=120)
    iron = models.CharField(max_length=120)
    sodium = models.CharField(max_length=120)
    glucose = models.CharField(max_length=120)
    calcium = models.CharField(max_length=120)


    def __str__(self):
        return f"{self.user} {self.food}"


class Exercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    exercise = models.CharField(max_length=120)
    duration = models.CharField(max_length=60)
    calories = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.user} {self.exercise}"
