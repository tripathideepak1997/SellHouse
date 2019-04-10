from django.urls import path
from .views import register_property, register_update, property_view, property_interiors

app_name = 'property'

urlpatterns = [
    path('property_register/', register_property, name='register'),
    path('property_update/<int:id>', register_update, name='update_property'),
    path('property_view/', property_view, name='property_view'),
    path('property_interior/<int:id>', property_interiors, name='property_interior'),
   ]
