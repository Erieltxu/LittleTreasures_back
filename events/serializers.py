from rest_framework import serializers
from .models import Event, EventRegistration


class EventRegistrationSerializer(serializers.ModelSerializer):
    child_name = serializers.CharField(source='child.first_name', read_only=True)

    class Meta:
        model = EventRegistration
        fields = ['id', 'child_name', 'registered_at']


class EventSerializer(serializers.ModelSerializer):
    registrations = EventRegistrationSerializer(many=True, read_only=True)
    remaining_spots = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'spots', 'remaining_spots', 'registrations']

    def get_remaining_spots(self, obj):
        return obj.spots - obj.registrations.count()
