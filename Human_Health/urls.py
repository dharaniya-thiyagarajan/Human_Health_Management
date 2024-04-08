
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Human_Health.views import sleepview
from .views import Foodview

router = DefaultRouter()
router.register("Sleep",sleepview,basename="Sleep"),
router.register("food",Foodview ,basename="Food")

urlpatterns=[
path("", include(router.urls)),
]