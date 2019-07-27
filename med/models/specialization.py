from django.db import models

__all__ = ['Specialization']


class Specialization(models.Model):
    name = models.CharField(
        verbose_name='Название', max_length=255,
    )

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return self.name
