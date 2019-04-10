from rest_framework import serializers

from keepitprivate.file_system.models import File


class FileSerializer(serializers.ModelSerializer):
    """ Serializer dedicated to the File model """

    class Meta:
        model = File
        fields = '__all__'
