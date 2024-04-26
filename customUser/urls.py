from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('profile<int:id_user>', views.profile, name='profile')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)