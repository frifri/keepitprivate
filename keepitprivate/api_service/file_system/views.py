from rest_framework import viewsets

from keepitprivate.api_service.file_system.serializers import FileSerializer
from keepitprivate.core.api_service.permissions import IsOwner
from keepitprivate.file_system.models import File


class FileViewSet(viewsets.ModelViewSet):
    """ ViewSet dedicated to the File model """

    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = (IsOwner,)
