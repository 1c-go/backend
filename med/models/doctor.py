from django.db import models

__all__ = ['Doctor']


class Doctor(models.Model):
    full_name = models.CharField(
        verbose_name='ФИО', max_length=250,
    )

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'

    def __str__(self):
        return self.full_name
