from .views import CandidateViewSet, CandidateStatisticView
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'candidate', CandidateViewSet)
router.register(r'candidate-statistic', CandidateStatisticView)

urlpatterns = router.urls
