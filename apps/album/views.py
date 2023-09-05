from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from apps.album.models import Album

from .serializer import AlbumSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.prefetch_related('songs').all()
    serializer_class = AlbumSerializer
    permission_classes = (AllowAny,)
