from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserLoginViewSet, UserRegistrationViewSet

router = DefaultRouter()
router.register(r'registration', UserRegistrationViewSet, basename='user-registration')
router.register(r'login', UserLoginViewSet, basename='user-login')

urlpatterns = [
    path('user/', include(router.urls)),
]

