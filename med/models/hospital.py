from django.db import models

__all__ = ['Hospital']


class Hospital(models.Model):
    name = models.CharField(
        verbose_name='Название', max_length=250,
    )
    address = models.CharField(
        verbose_name='Адрес', max_length=250,
    )

    class Meta:
        verbose_name = 'Больница'
        verbose_name_plural = 'Больницы'

    def __str__(self):
        return self.name
