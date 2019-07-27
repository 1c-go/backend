from django.db import models

__all__ = ['Division']


class Division(models.Model):
    hospital = models.ForeignKey(
        verbose_name='Больница', to='med.Hospital', on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Название', max_length=100,
    )

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def __str__(self):
        return self.name
