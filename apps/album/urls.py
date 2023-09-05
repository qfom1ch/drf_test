from django.urls import include, path
from rest_framework import routers

from .views import AlbumViewSet

app_name = 'album'

router = routers.SimpleRouter()
router.register(r'', AlbumViewSet)

urlpatterns = [
    path('', include(router.urls), name='album'),
]
