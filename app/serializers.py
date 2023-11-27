
from rest_framework import serializers
from app.models import *
class VillagemodelSerializers(serializers.ModelSerializer):
    class Meta:
        model=VillageData
        fields='__all__'