from django.urls import include, path
from rest_framework import routers

from .views import SongViewSet

app_name = 'song'

router = routers.SimpleRouter()
router.register(r'', SongViewSet)

urlpatterns = [
    path('', include(router.urls), name='song'),

]
