
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customUser import views
urlpatterns = [
    path('', views.login, name="index"),
    path('admin/', admin.site.urls),
    path('usuarios/', include('customUser.urls')),
    path('publish/', include('publish.urls')),
    path('comment/<int:id_post>', include('comments.urls')),
    path('like/<int:id_post>', include('like.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
