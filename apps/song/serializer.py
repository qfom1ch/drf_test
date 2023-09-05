from rest_framework import serializers

from apps.album.serializer import AlbumSerializer
from apps.song.models import Song, SongsAlbums


class SongSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Song
        fields = (
            'id',
            'title',
            'albums',
        )


class SongsAlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongsAlbums
        fields = (
            'id',
            'album',
            'song',
            'song_number'
        )
