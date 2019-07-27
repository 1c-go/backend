from rest_framework import routers

from .views import RecordsViewSet
from .views import SpecializationsViewSet
from .views import HospitalsViewSet
from .views import DoctorsViewSet

router = routers.DefaultRouter()
router.register('records', RecordsViewSet)
router.register('hospitals', HospitalsViewSet)
router.register('specializations', SpecializationsViewSet)
router.register('doctors', DoctorsViewSet)
