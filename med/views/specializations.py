from django_filters import FilterSet, filters
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from med.serializers.specialization import SpecializationSerializer
from ..models import Specialization

__all__ = ['SpecializationsViewSet']


class SpecializationFilterSet(FilterSet):
    hospital = filters.NumberFilter(field_name='position__division__hospital')


class SpecializationsViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    filterset_class = SpecializationFilterSet
