from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..models import Hospital, calc_rate
from ..serializers.hospital import HospitalSerializer

__all__ = ['HospitalsViewSet']


class HospitalsViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = calc_rate(Hospital.objects)
    serializer_class = HospitalSerializer
