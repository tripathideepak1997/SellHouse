from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('fun/', fun, name='success_page'),
    path('register/', register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
