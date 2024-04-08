from rest_framework import serializers
from Human_Health.models import sleep

class sleepserializers(serializers.ModelSerializer):
    
    class Meta:
        model=sleep
        fields="__all__"