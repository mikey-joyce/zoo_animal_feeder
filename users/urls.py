"""Defines the URL patterns of the users"""

from django.urls import path
from django.contrib.auth.views import login
from . import views

app_name = 'users'
urlpatterns = [
    #Login Page
    path('login/', login, {'template_name':'users/login.html'}, name='login'),

    #Logout page
    path('logout/', views.logout_view, name='logout'),
]