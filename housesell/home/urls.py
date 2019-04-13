from django.contrib import admin
from django.urls import path, include
from .views import Base, search_property, enquire_property, property_listings

app_name = "home"

urlpatterns = [
    path('home/', Base.as_view(), name='base'),
    path('search/', search_property, name='search'),
    path('enquiry_req/<int:id>', enquire_property, name='enquire'),
    path('property_listing/', property_listings, name='property_list'),
]
