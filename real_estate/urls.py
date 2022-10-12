from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
urlpatterns = [
    path('supercrect/', admin.site.urls),    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
