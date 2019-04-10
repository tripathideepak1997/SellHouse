from django.contrib import admin
from django.urls import path, include
from .views import Base, search_property

app_name = "home"

urlpatterns = [
    path('home/', Base.as_view(), name='base'),
    path('search/', search_property, name='search')
]
