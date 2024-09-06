from django.urls import path, include
from rest_framework import routers
from .views import EventView


router = routers.DefaultRouter()
router.register('events', EventView, 'events')

urlpatterns = [
    path('', include(router.urls)),
]
