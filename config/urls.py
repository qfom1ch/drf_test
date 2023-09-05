"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from apps.song.views import AddSongToAlbum

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="Тестовое задание",
        contact=openapi.Contact(email="fomichev.ser.v@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/singer/', include('apps.singer.urls', namespace='api_singer')),
    path('api/v1/song/', include('apps.song.urls', namespace='api_song')),
    path('api/v1/album/', include('apps.album.urls', namespace='api_album')),
    path('api/v1/add_song_to_album/', AddSongToAlbum.as_view(), name='add_song_to_album'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
