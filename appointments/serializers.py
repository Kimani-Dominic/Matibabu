from rest_framework import serializers

from appointments.models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'appointment_time', 'status', 'created_at']
        
        
        
        def validate_user(self, value):
            if not value:
                raise serializers.ValidationError("User Must be authenticated to make an appointment")
            return value
        