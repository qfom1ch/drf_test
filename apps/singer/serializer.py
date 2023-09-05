from rest_framework import serializers

from apps.singer.models import Singer


class SingerSerializer(serializers.ModelSerializer):
    albums = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Singer
        fields = (
            'id',
            'name',
            'albums'
        )
