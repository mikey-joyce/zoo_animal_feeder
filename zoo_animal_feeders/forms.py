from django import forms

from .models import AnimalType, Animal, Schedule

class TypeForm(forms.ModelForm):
	
	class Meta:
		model = AnimalType
		fields = ['a_type', 'date_added']
		labels = {'a_type':''}

class AnimalForm(forms.ModelForm):
	
	class Meta:
		model = Animal
		fields = ['animal_type', 'name', 'date_added']
		labels = {'name':''}
		widgets = {'name': forms.Textarea(attrs={'cols':40})}

class ScheduleForm(forms.ModelForm):

	class Meta:
		model = Schedule
		fields = ['breakfast', 'lunch', 'dinner']
		labels = {'breakfast':'','lunch':'','dinner':''}
