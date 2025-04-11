from rest_framework import serializers

from appointments.models import Appointment
from .models import MedicalRecord

class MedicalRecordSerializer(serializers.ModelSerializer):
    appointment = serializers.PrimaryKeyRelatedField(queryset=Appointment.objects.all())

    class Meta:
        model = MedicalRecord
        fields = ['appointment', 'diagnosis', 'prescription', 'treatment', 'notes']
        read_only_fields = ['patient', 'appointment']
        
        
    
    def validate_appointment(self, value):
        if not Appointment.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Appointment does not exist.")
        return value
    
    def create(self, validated_data):
        appointment = validated_data['appointment']
        validated_data['patient'] = appointment.user 
        return super().create(validated_data)
    
    def validate_user(self, value):
                if not value:
                    raise serializers.ValidationError("User Must be authenticated")
                return value