from rest_framework import viewsets
from Human_Health.models import Food,Water,Sleep,Walk,Mobile,Location
from .serializers import Foodserializer,Waterserializer,Sleepserializer,Walkserializer,Mobileserializer,Locationserializer

def food(request):
    pass

class Foodview(viewsets.ModelViewSet):
    queryset= Food.objects.all()
    serializer_class=Foodserializer
    http_method_names=["get","post","put","delete"]



def water(request):
    pass

class Waterview(viewsets.ModelViewSet):
 queryset=Water.objects.all()
 serializer_class=Waterserializer
 http_method_names=["get","post","put","delete"]



 def Sleep(request):
    pass

class Sleepview(viewsets.ModelViewSet):
 queryset=Sleep.objects.all()
 serializer_class=Sleepserializer
 http_method_names=["get","post","put","delete"]   



 def Walk(request):
    pass

class Walkview(viewsets.ModelViewSet):
 queryset=Walk.objects.all()
 serializer_class=Walkserializer
 http_method_names=["get","post","put","delete"]   


 def Mobile(request):
    pass

class Mobileview(viewsets.ModelViewSet):
 queryset=Mobile.objects.all()
 serializer_class=Mobileserializer
 http_method_names=["get","post","put","delete"]   


 def Location(request):
    pass

class Locationview(viewsets.ModelViewSet):
 queryset=Location.objects.all()
 serializer_class=Locationserializer
 http_method_names=["get","post","put","delete"]   
