from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from aa import serializers
from aa.models import Avt

class AvtModelViewSet(viewsets.ModelViewSet):
      queryset = Avt.objects.all()
      serializer_class = serializers.AvtModelSerializer

      def get_permissions(self):
          if self.request.method == 'GET':
              return [AllowAny()]
          return [IsAuthenticated()]

      def perform_create(self, serializer):
          serializer.save(user=self.request.user)
