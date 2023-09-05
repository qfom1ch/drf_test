from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny

from apps.song.models import Song, SongsAlbums

from .serializer import SongsAlbumsSerializer, SongSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.prefetch_related('albums').all()
    serializer_class = SongSerializer
    permission_classes = (AllowAny,)


class AddSongToAlbum(generics.CreateAPIView):
    queryset = SongsAlbums.objects.all()
    serializer_class = SongsAlbumsSerializer
