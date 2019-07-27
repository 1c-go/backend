from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..models import Hospital
from ..serializers.hospital import HospitalSerializer

__all__ = ['HospitalsViewSet']


class HospitalsViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
