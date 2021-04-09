from rest_framework import routers
from .api import DriverViewSet, UserViewSet, LocationViewSet, SponsorViewSet, RideViewSet

router = routers.DefaultRouter()
router.register('api/Driver', DriverViewSet)
router.register('api/User', UserViewSet)
router.register('api/Location', LocationViewSet)
router.register('api/Sponsor', SponsorViewSet)
router.register('api/Ride', RideViewSet)

urlpatterns = router.urls
