from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RideViewSet

router = DefaultRouter()
router.register(r'rides', RideViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rides/<int:pk>/start/', RideViewSet.as_view({'put': 'start_ride'}), name='ride-start'),
    path('rides/<int:pk>/complete/', RideViewSet.as_view({'put': 'complete_ride'}), name='ride-complete'),
    path('rides/<int:pk>/cancel/', RideViewSet.as_view({'put': 'cancel_ride'}), name='ride-cancel'),
]