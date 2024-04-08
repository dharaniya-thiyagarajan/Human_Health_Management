from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Foodview


router= DefaultRouter()
router.register("food",Foodview ,basename="Food")

urlpatterns=[
path("", include(router.urls)),
]