from .views import ReferendumViewSet, CitizenViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'referendum', ReferendumViewSet)
router.register(r'citizens', CitizenViewSet)

urlpatterns = router.urls