"""Defines URL patterns for zoo_animal_feeders"""

from django.urls import path
from . import views

app_name = 'zoo_animal_feeders'
urlpatterns = [
    #This is for the home page
    path('', views.index, name='index'),

    #Show animal types
    path('animal_types/', views.animal_types, name='animal_types'),

    #Page that will access a certain category of animals
    path('animal_types/<int:animal_type_id>/', views.animal_type, name='animal_type'),

    #Page for accessing an animal (and its schedule)
    path('animal/<int:animal_id>/', views.animal, name='animal'),

    #Page for adding a new animal type
    path('new_animal_type/', views.new_animal_type, name='new_animal_type'),

    #Page for adding a new animal
    path('new_animal/<int:animal_type_id>/', views.new_animal, name='new_animal'),

    #page for adding a new schedule
    path('new_schedule/<int:animal_id>/', views.new_schedule, name='new_schedule'),

    #page for editing an animal
    path('edit_animal/<int:animal_id>/', views.edit_animal, name='edit_animal'),

    #page for editing a schedule
    path('edit_schedule/<int:schedule_id>/', views.edit_schedule, name='edit_schedule'),
]
