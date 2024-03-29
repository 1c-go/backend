from django_filters import FilterSet, filters
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..models import Specialization
from ..serializers.specialization import SpecializationSerializer

__all__ = ['SpecializationsViewSet']


class SpecializationFilterSet(FilterSet):
    hospital = filters.NumberFilter(field_name='position__division__hospital', distinct=True)


class SpecializationsViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Specialization.objects.order_by('name')
    serializer_class = SpecializationSerializer
    filterset_class = SpecializationFilterSet
