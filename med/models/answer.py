from django.db import models

__all__ = ['Answer']


class Answer(models.Model):
    record = models.ForeignKey(
        verbose_name='Заявка', to='med.Record', on_delete=models.PROTECT,
    )
    question = models.ForeignKey(
        verbose_name='Вопрос', to='med.Question', on_delete=models.PROTECT,
    )
    answer = models.BooleanField(
        verbose_name='Ответ', null=True, blank=True,
    )

    class Meta:
        verbose_name = 'Ответ на вопрос'
        verbose_name_plural = 'Ответы на вопросы'

    def __str__(self):
        return f'{self.record} - {self.question}'
