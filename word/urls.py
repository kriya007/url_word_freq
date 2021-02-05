from django.contrib import admin
from django.urls import path
from word import views

urlpatterns = [
    path("", views.index, name = 'word'),
    
]