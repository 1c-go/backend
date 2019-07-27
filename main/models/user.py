from django.contrib.auth.models import AbstractUser
from django.db import models

__all__ = ['CustomUser']


class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    full_name = models.CharField(
        verbose_name='ФИО', max_length=250,
    )

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name

    def __str__(self):
        return self.full_name
