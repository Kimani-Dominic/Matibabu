from rest_framework import serializers

from doctors.models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['specialization', 'available_days', 'available_hours']
        
        def validate_user(self, value):
            if not value:
                raise serializers.ValidationError("User Must be authenticated")
            return value