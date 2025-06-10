from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static  # Importa para servir archivos media

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalogo.urls')),  # Enruta a la app "catalogo"
]

# Sirve archivos multimedia (imágenes, etc.) en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






