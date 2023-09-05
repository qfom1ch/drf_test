from rest_framework import serializers

from apps.album.models import Album


class AlbumSerializer(serializers.ModelSerializer):
    songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Album
        fields = (
            'id',
            'singer',
            'year_of_issue',
            'songs'
        )
