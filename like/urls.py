from django.urls import path
from . import views

urlpatterns = [
    path('add_like', views.add_like, name='add_like'),
]