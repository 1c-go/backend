from rest_framework import mixins, decorators, serializers
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from med.models import Record
from med.serializers.record import RecordCreateSerializer, RecordSerializer

__all__ = ['RecordsViewSet']


class RateParser(serializers.Serializer):
    rate = serializers.IntegerField(min_value=1, max_value=10)


class RecordsViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin):
    queryset = Record.objects.all()

    def get_queryset(self):
        return Record.objects.filter(patient__user=self.request.user)

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return RecordSerializer
        return RecordCreateSerializer

    @decorators.action(methods=('POST',), detail=True)
    def rate(self, request, *args, **kwargs):
        record = self.get_object()
        if record.status != Record.AWAITING_RATE:
            raise ValidationError('Можно оценить только заявку, ожидающую оценку')
        serializer = RateParser(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as error:
            return Response({'success': False, 'errors': error.detail})
        record.rate = serializer.validated_data['rate']
        record.status = Record.CLOSED
        record.save()
        return Response({'success': True})

    @decorators.action(methods=('POST',), detail=True)
    def cancel(self, request, *args, **kwargs):
        record = self.get_object()
        if record.status != Record.OPENED:
            raise ValidationError('Можно закрыть только открытую заявку')
        record.status = Record.CANCELED
        record.save()
