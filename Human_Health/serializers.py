from rest_framework import serializers
from Human_Health.models import Food

class Foodserializer (serializers.ModelSerializer):
     class Meta:
          model=Food
          fields="__all__"