from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
app_name = "blogapp"

urlpatterns = [
    path('fun/', fun, name='success_page'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('enquire_views/', view_enquiries, name='view_enquiries'),
    path('property_view/<int:id>', property_view_enquire, name='property_view'),
]
