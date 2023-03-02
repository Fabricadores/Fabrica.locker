from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from FabricaLocker.views import LockerViewSet

router = DefaultRouter()
router.register(r"Rfid", LockerViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]