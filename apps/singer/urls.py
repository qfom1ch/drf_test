from django.urls import include, path
from rest_framework import routers

from .views import SingerViewSet

app_name = 'singer'

router = routers.SimpleRouter()
router.register(r'', SingerViewSet)

urlpatterns = [
    path('', include(router.urls), name='singer'),
]
