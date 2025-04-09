from rest_framework import serializers
from Auth.models import User
from patients.models import Patient
        
        
class PatientSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Patient
        fields = ['dob', 'phone', 'address', 'insurance_provider', 'insurance_number']
 
        
        def validate_user(self, value):
            if not value:
                raise serializers.ValidationError("User Must be authenticated")
            return value
       