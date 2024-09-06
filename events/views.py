from rest_framework import viewsets, permissions
from rest_framework import viewsets, permissions
from .models import Event
from .serializers import EventSerializer


# Create your views here.
class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super(EventView, self).get_permissions()