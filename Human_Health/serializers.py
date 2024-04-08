from rest_framework import serializers
from Human_Health.models import sleep

class sleepserializers(serializers.ModelSerializer):
    
    class Meta:
        model=sleep
        fields="__all__"
from Human_Health.models import Food

class Foodserializer (serializers.ModelSerializer):
     class Meta:
          model=Food
          fields="__all__"
