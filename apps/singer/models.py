from django.db import models


class Singer(models.Model):
    name = models.CharField('Никнейм', max_length=150, unique=True)

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнитель'
        ordering = 'name',

    def __str__(self):
        return self.name
