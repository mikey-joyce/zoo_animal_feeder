from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AnimalType(models.Model):
    """Type of animal that can classify the animal"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    a_type = models.CharField(max_length=50, default='')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.a_type

class Animal(models.Model):
    """The actual animal, embeded in animaltype"""
    animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, default='')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.name)>20:
            return self.name[:20] + "..."
        else:
            return self.name

class Schedule(models.Model):
    """Model for animal eating schedule"""
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)
    breakfast = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
