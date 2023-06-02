from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('bourse.urls')),
    path('user', include('user.urls')),
    # Autres URLs de l'application principale
]

# Ajoutez le bloc suivant uniquement si vous utilisez les médias en mode DEBUG
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
