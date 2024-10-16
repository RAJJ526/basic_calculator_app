from django.contrib import admin
from django.urls import path
from calculator import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jods/', views.jod, name='jods'),
]