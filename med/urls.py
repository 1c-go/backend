from rest_framework import routers

from .views import DoctorsViewSet
from .views import HospitalsViewSet
from .views import RecordsViewSet
from .views import SpecializationsViewSet

router = routers.DefaultRouter()
router.register('records', RecordsViewSet)
router.register('hospitals', HospitalsViewSet)
router.register('specializations', SpecializationsViewSet)
router.register('doctors', DoctorsViewSet)
