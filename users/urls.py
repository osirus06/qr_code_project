from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ScanQRViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'auth', ScanQRViewSet, basename="auth")
urlpatterns = router.urls
