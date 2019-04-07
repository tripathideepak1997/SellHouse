from django.contrib import admin
from django.urls import path, include
from .views import Base
app_name = "home"

urlpatterns = [
    path('home/', Base.as_view(), name='base'),
]
