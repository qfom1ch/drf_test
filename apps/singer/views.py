from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from apps.singer.models import Singer

from .serializer import SingerSerializer


class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.prefetch_related('albums').all()
    serializer_class = SingerSerializer
    permission_classes = (AllowAny,)
