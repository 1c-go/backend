from rest_framework import mixins, decorators, serializers
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import Record
from ..models import Question
from ..models import Answer
from ..serializers.record import RecordCreateSerializer, RecordSerializer
from ..serializers.question import QuestionSerializer

__all__ = ['RecordsViewSet']


class AnswerParser(serializers.Serializer):
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects)
    answer = serializers.BooleanField()


class AnswersParser(serializers.Serializer):
    answers = AnswerParser(many=True)


class RecordsViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin):
    queryset = Record.objects.all()

    def get_queryset(self):
        return Record.objects.filter(patient__user=self.request.user)

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return RecordSerializer
        return RecordCreateSerializer

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user.patient_set.first())

    @decorators.action(methods=('POST',), detail=True)
    def cancel(self, request, *args, **kwargs):
        record = self.get_object()
        if record.status != Record.OPENED:
            raise ValidationError('Можно закрыть только открытую заявку')
        record.status = Record.CANCELED
        record.save()

    @decorators.action(methods=('GET',), detail=True)
    def questions(self, request, *args, **kwargs):
        record = self.get_object()
        if record.status != record.AWAITING_RATE:
            raise ValidationError('Можно ')
        answers = record.answer_set.all()
        if not answers:
            questions_spec = Question.random_manager.for_specialization(record.specialization)
            questions_div = Question.random_manager.for_division()
            questions_hospital = Question.random_manager.for_hospital()
            questions = questions_spec | questions_div | questions_hospital

            Answer.objects.bulk_create([
                Answer.objects.create(record=record, question=question)
                for question in questions
            ])
        else:
            questions = Question.objects.filter(answer__record=record)

        return QuestionSerializer(questions, many=True).data

    @decorators.action(methods=('POST',), detail=True)
    def answer(self, request, *args, **kwargs):
        record = self.get_object()

        if record.status != Record.AWAITING_RATE:
            raise ValidationError('Можно оценить только заявку, ожидающую оценку')

        serializer = AnswersParser(data=request.data)
        serializer.is_valid(raise_exception=True)

        for pair in serializer.validated_data:
            answer = Answer.objects.get(record=record, question=pair['question'])
            answer.answer = pair['answer']
            answer.save()

        record.status = Record.CLOSED
        record.save()
        return Response({})
