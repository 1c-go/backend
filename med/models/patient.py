from django.db import models
from django.conf import settings

__all__ = ['Patient']


class Patient(models.Model):
    user = models.ForeignKey(
        verbose_name='Пользователь', to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
    )
    default_hospital = models.ForeignKey(
        verbose_name='Больница по умолчанию', to='med.Hospital', on_delete=models.SET_NULL,
        null=True, blank=True,
    )

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациент'

    def __str__(self):
        return self.user.full_name
