from rest_framework import serializers

from aa.models import Avt


class AvtModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avt
        fields = ['id', 'text', 'created_at']
        read_only_fields = ['id', 'created_at', 'user']

