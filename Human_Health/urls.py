
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Human_Health.views import sleepview

router = DefaultRouter()
router.register("Sleep",sleepview,basename="Sleep"
)

urlpatterns = [
    path("",include(router.urls)),
]