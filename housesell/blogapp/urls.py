from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('fun/', fun, name='fun'),
    path('register/', register, name='register'),
]
