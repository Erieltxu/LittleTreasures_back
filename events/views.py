from rest_framework import viewsets, permissions, serializers
from .models import Event, EventRegistration, Child
from .serializers import EventSerializer, EventRegistrationSerializer
from rest_framework.exceptions import ValidationError


class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()


class EventRegistrationView(viewsets.ModelViewSet):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        data = self.request.data
        event_id = data.get('event')
        child_id = data.get('child')

        # Verificar si los datos existen
        if event_id is None or child_id is None:
            raise ValidationError('El campo "event" y "child" son obligatorios.')

        try:
            event = Event.objects.get(id=event_id)
            child = Child.objects.get(id=child_id)
        except Event.DoesNotExist:
            raise ValidationError('El evento especificado no existe.')
        except Child.DoesNotExist:
            raise ValidationError('El niño especificado no existe.')

        # Verificar plazas disponibles
        if event.spots > event.registrations.count():
            # Aquí se guarda el campo `user` automáticamente
            serializer.save(user=self.request.user)
        else:
            raise ValidationError('No hay plazas disponibles.')