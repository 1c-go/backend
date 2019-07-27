from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..serializers.hospital import HospitalSerializer
from ..models import Hospital

__all__ = ['HospitalsViewSet']


class HospitalsViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
