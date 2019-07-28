from django.db import models

__all__ = ['Position']


class Position(models.Model):
    doctor = models.ForeignKey(
        verbose_name='Доктор', to='med.Doctor', on_delete=models.CASCADE,
    )
    division = models.ForeignKey(
        verbose_name='Подразделение', to='med.Division', on_delete=models.PROTECT,
    )
    specialization = models.ForeignKey(
        verbose_name='Специализация', to='med.Specialization', on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = 'Рабочее место'
        verbose_name_plural = 'Рабочие места'

    def __str__(self):
        return f'{self.doctor} - {self.division} - {self.specialization}'
