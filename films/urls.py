from django.urls import path, include
from .views import *

urlpatterns = [
    path('', FilmsGallery.as_view(), name='card'),
]