from django.db import models

__all__ = ['Question']


# по специализации, по больнице, по подразделению
# специалист: specialization, hospital=False
# подразделение: specialization=null, hospital=False
# больница: specialization=null, hospital=True


class QuestionManager(models.Manager):
    DEFAULT_COUNT = 2

    def _random(self, queryset, count=DEFAULT_COUNT):
        return queryset.order_by('?')[:count]

    def for_specialization(self, specialization, count=DEFAULT_COUNT):
        qs = super().get_queryset().filter(specialization=specialization, hospital=False)
        return self._random(qs, count)

    def for_division(self, count=DEFAULT_COUNT):
        qs = super().get_queryset().filter(specialization=None, hospital=False)
        return self._random(qs, count)

    def for_hospital(self, count=DEFAULT_COUNT):
        qs = super().get_queryset().filter(specialization=None, hospital=True)
        return self._random(qs, count)


class Question(models.Model):
    name = models.CharField(
        verbose_name='Название', max_length=250,
    )
    specialization = models.ForeignKey(
        verbose_name='Специализация', to='med.Specialization', on_delete=models.PROTECT,
        null=True, blank=True,
    )
    hospital = models.BooleanField(
        verbose_name='Вопрос о больнице'
    )
    question = models.TextField(
        verbose_name='Вопрос',
    )
    positive_answer = models.BooleanField(
        verbose_name='Положительный ответ',
    )

    objects = models.Manager()
    random_manager = QuestionManager()

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.name
