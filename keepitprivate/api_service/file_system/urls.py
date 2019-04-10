from rest_framework import routers

from keepitprivate.api_service.file_system.views import FileViewSet

router = routers.DefaultRouter()
router.register('files', FileViewSet)

urlpatterns = router.urls
