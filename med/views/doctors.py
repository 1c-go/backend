from django_filters import FilterSet, filters
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..models import Doctor
from ..serializers.doctor import DoctorSerializer

__all__ = ['DoctorsViewSet']


class DoctorFilterSet(FilterSet):
    hospital = filters.NumberFilter(field_name='position__division__hospital', distinct=True)
    specialization = filters.NumberFilter(field_name='position__specializations', distinct=True)


class DoctorsViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filterset_class = DoctorFilterSet
