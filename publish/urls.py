from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('delete_post/<int:id_post>', views.delete_post, name='delete_post')
]
