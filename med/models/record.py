from django.db import models

__all__ = ['Record']


class Record(models.Model):
    OPENED = 1
    AWAITING_RATE = 2
    CLOSED = 3
    CANCELED = 4
    _status_choices = (
        (OPENED, 'Открыта'),
        (AWAITING_RATE, 'Ждет оценку'),
        (CLOSED, 'Закрыта'),
        (CANCELED, 'Отменена')
    )

    patient = models.ForeignKey(
        verbose_name='Пациент', to='med.Patient', on_delete=models.PROTECT,
    )
    hospital = models.ForeignKey(
        verbose_name='Больница', to='med.Hospital', on_delete=models.PROTECT,
    )
    specialization = models.ForeignKey(
        verbose_name='Специализация', to='med.Specialization', on_delete=models.PROTECT,
    )
    doctor = models.ForeignKey(
        verbose_name='Доктор', to='med.Doctor', on_delete=models.PROTECT,
    )
    opened_at = models.DateTimeField(
        verbose_name='Дата-время открытия', auto_now_add=True,
    )
    recording_at = models.DateTimeField(
        verbose_name='Дата-время записи',
    )
    closed_at = models.DateTimeField(
        verbose_name='Дата-время закрытия', null=True, blank=True,
    )
    title = models.CharField(
        verbose_name='Тема', max_length=100,
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    status = models.PositiveSmallIntegerField(
        verbose_name='Статус', default=OPENED, choices=_status_choices,
    )

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.patient} - {self.recording_at.strftime("%Y.%m.%d %H:%M")}'
