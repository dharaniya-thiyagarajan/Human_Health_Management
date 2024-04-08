from rest_framework import serializers
from .models import Food,Water,Sleep,Walk,Mobile,Location

class Foodserializer (serializers.ModelSerializer):
     class Meta:
          model=Food
          fields="__all__"


class Waterserializer (serializers.ModelSerializer) :
     class Meta:
          model=Water 
          fields="__all__"    

class Sleepserializer (serializers.ModelSerializer) :
     class Meta:
          model=Sleep 
          fields="__all__"     

class Walkserializer (serializers.ModelSerializer) :
     class Meta:
          model=Walk 
          fields="__all__"    

class Mobileserializer(serializers.ModelSerializer):                  
   class Meta:
          model=Mobile 
          fields="__all__"  

class Locationserializer(serializers.ModelSerializer):                  
   class Meta:
          model=Location
          fields="__all__"           