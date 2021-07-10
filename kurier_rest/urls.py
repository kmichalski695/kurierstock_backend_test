from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RowerViewSet

router = DefaultRouter()
router.register(r'rowery', RowerViewSet, basename='Rowery')

urlpatterns = [
    path("", include(router.urls))
]