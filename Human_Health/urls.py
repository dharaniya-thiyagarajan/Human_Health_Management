from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Foodview,Waterview,Sleepview,Walkview,Mobileview,Locationview


router= DefaultRouter()
router.register("food",Foodview ,basename="Food")
router.register("water",Waterview ,basename="Water")
router.register("sleep",Sleepview ,basename="Sleep")
router.register("Walk",Walkview ,basename="Walk")
router.register("Mobile",Mobileview ,basename="Mobile")
router.register("Location",Locationview ,basename="Location")
urlpatterns=[
path("", include(router.urls)),
]