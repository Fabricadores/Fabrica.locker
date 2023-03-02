from rest_framework.serializers import ModelSerializer
from FabricaLocker.models import rfidTags



class LockerSerializer(ModelSerializer):
    class Meta:
        model = rfidTags
        fields = '__all__'
