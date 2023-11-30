from django.urls import path
from .views import *
urlpatterns = [
    path('',meals, name='meals'),
]
