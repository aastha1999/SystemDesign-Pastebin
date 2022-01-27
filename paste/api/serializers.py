from rest_framework import serializers
from paste.models import PasteFile

class PasteFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasteFile
        fields = ['title','content']