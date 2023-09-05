from datetime import datetime

from django.core.validators import MaxValueValidator
from django.db import models


class Album(models.Model):
    singer = models.ForeignKey('singer.Singer',
                               on_delete=models.CASCADE,
                               related_name='albums',
                               verbose_name='Исполнитель', null=True, blank=True)
    songs = models.ManyToManyField('song.Song', through='song.SongsAlbums')

    year_of_issue = models.PositiveIntegerField(validators=[MaxValueValidator(datetime.now().year)], default=None)

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return self.year_of_issue
