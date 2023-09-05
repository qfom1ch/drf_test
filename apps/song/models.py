from django.db import models


class Song(models.Model):
    title = models.CharField('Название', max_length=150, unique=True)
    albums = models.ManyToManyField('album.Album', through='SongsAlbums')

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'
        ordering = 'title',

    def __str__(self):
        return self.title


class SongsAlbums(models.Model):
    song = models.ForeignKey('song.Song', on_delete=models.CASCADE, related_name='songs')
    album = models.ForeignKey('album.Album', on_delete=models.CASCADE)
    song_number = models.PositiveIntegerField()
