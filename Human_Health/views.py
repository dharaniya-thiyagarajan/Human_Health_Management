from rest_framework import viewsets
from Human_Health.models import Food
from .serializers import Foodserializer

def food(request):
    pass

class Foodview(viewsets.ModelViewSet):
    queryset= Food.objects.all()
    serializer_class=Foodserializer
    http_method_names=["get","post","put","delete"]
