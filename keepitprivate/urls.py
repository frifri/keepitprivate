"""
keepitprivate base URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from keepitprivate.constants import DEV

urlpatterns = [
    path('auth/', include('keepitprivate.api_service.auth.urls')),
    path('file_system/', include('keepitprivate.api_service.file_system.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.ENVIRONMENT == DEV:
    urlpatterns += [
        path('api-auth/', include('rest_framework.urls')),
    ]
