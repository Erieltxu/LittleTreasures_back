from rest_framework import viewsets, permissions, serializers  # Asegúrate de que serializers está importado
from .models import Event, EventRegistration
from .serializers import EventSerializer, EventRegistrationSerializer

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
        # Restar una plaza del evento al inscribir
        event = serializer.validated_data['event']
        if event.spots > event.registrations.count():
            serializer.save(user=self.request.user)
        else:
            raise serializers.ValidationError('No hay plazas disponibles.')
