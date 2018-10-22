from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
	"""log out"""
	logout(request)
	return HttpResponseRedirect(reverse('zoo_animal_feeders:index'))

def register(request):
	"""registers a new user"""
	if request.method != 'POST':
		#displays blank form
		form = UserCreationForm()
	else:
		#process the filled out form
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			#log user in and send them to the home page
			authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
			login(request, authenticated_user)
			return HttpResponseRedirect(reverse('zoo_animal_feeders:index'))

	context = {'form':form}
	return render(request, 'users/register.html', context)
