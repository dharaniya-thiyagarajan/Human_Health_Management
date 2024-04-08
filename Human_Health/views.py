from rest_framework import viewsets
from Human_Health.models import sleep
from Human_Health.serializers import sleepserializers

def food(request):
    pass

# Create your views here.
class sleepview(viewsets.ModelViewSet):
    queryset = sleep.objects.all()
    serializer_class = sleepserializers
    http_method_names = ["get","post","put","delete"]

