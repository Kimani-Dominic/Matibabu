from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, generics, status, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from patients.models import Patient
from patients.serializers import PatientSerializer
class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # return super().get_queryset()
        return Patient.objects.filter(user=self.request.user)

    
class RegisterPatientInfo(generics.CreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # def get_queryset(self):
    #     return Patient.objects.filter(user__is_patient=True)
    
    def create(self, request, *args, **kwargs):
        user = request.user
        
        if Patient.objects.filter(user=user).exists():
            return Response({"error: You can only update your profile"}, status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            # self.perform_create(serializer)
            return Response({"message": "Patients Profile updated successfuly"}, status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
class UpdatePatientInfo(generics.UpdateAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Patient.objects.get(user=self.request.user)
    
    def update(self, request, *args, **kwargs):
        instance = get_object_or_404(Patient, user=request.user)  
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Patient Profile updated successfully"}, status=status.HTTP_200_OK)
    