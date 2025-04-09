from rest_framework import serializers
from django.contrib.auth.models import Group

from .models import *
from django.contrib.auth import authenticate, get_user_model


User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=[(''), ('doctor', 'Doctor'), ('patient', 'Patient')])
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'role']
        
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with ethe email already exists")
        return value
    
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match!")
        return data 
    
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        role = validated_data.pop('role')
        user.save()
        # role = validated_data.pop('role')
        # role_group = Group.objects.get(name=role) 
        # user.groups.add(role_group)

        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid login credentials")
        return user
    
    