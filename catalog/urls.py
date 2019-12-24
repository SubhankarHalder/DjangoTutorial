from django.urls import path
from . import views

urlpatterns = [
    # Calls the view function that is a function named index() in views.py file 
    path('', views.index, name='index'),
]