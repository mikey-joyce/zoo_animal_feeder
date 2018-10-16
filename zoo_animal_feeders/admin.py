from django.contrib import admin

# Register your models here.

from zoo_animal_feeders.models import AnimalType, Animal, Schedule

admin.site.register(AnimalType)
admin.site.register(Animal)
admin.site.register(Schedule)

