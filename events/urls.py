from django.urls import path, include
from rest_framework import routers
from .views import EventView, EventRegistrationView

router = routers.DefaultRouter()
router.register('events', EventView, 'events')
router.register('registrations', EventRegistrationView, 'registrations')

urlpatterns = [
    path('', include(router.urls)),
]
