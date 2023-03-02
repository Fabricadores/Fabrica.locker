from rest_framework.viewsets import ModelViewSet

from FabricaLocker.models import rfidTags
from FabricaLocker.serializers import LockerSerializer

class LockerViewSet(ModelViewSet):
    queryset = rfidTags.objects.all()
    serializer_class = LockerSerializer


# class CategoriaViewSet(ModelViewSet):
#     queryset = Categoria.objects.all()
#     serializer_class = CategoriaSerializer