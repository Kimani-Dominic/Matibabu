from django.shortcuts import render
# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema


from Auth.models import User
from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer


# class CreateAppointmentView(APIView):
#     serializer_class = AppointmentSerializer
#     permission_classes = [IsAuthenticated]


   
#     def post(self, request, *args, **kwargs):
#         serializer = AppointmentSerializer(data=request.data)
        
#         if not request.user.groups.filter(name='patient').exists():
#             return Response({"error": "Only patients can create appointments."}, status.HTTP_403_FORBIDDEN)

#         # Check if the doctor is available at the requested time
#         doctor_id = request.data.get('doctor')
#         doctor = User.objects.get(id=doctor_id)
#         if not doctor.groups.filter(name='doctor').exists():
#             return Response({Selected user isn't a doctor})
        
#         appointment_time = request.data.get('appointment_time')
#         if Appointment.objects.filter(doctor_id=doctor_id, appointment_time=appointment_time).exists():
#             return Response({"error": "Doctor is already boked at this time."}, status.HTTP_400_BAD_REQUEST)
        
#         if serializer.is_valid():
#             appointment = serializer.save()
#             return Response(AppointmentSerializer(appointment).data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
class CreateAppointmentView(APIView):
    #  Ensures that only authenticated users can create appointments.
    permission_classes = [IsAuthenticated]  
    @swagger_auto_schema(operation_description="Create a new appointment.")
    def post(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='patient').exists():
            return Response({"error": "Only users with user role patients can create appointments."}, status.HTTP_403_FORBIDDEN)

        appointment_time = request.data.get('appointment_time')

        # Find an available doctor who is not already booked at this time
        available_doctor = User.objects.filter(groups__name='doctor').exclude(
            appointments__appointment_time=appointment_time
        ).first()

        if not available_doctor:
            return Response({"error": "No doctors available at this time."}, status.HTTP_400_BAD_REQUEST)

        data = {
            **request.data, 
            'doctor': available_doctor.id,
        }

        serializer = AppointmentSerializer(data=data)
        if serializer.is_valid():
            appointment = serializer.save(user=request.user)
            return Response(AppointmentSerializer(appointment).data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class AppointmentListView(ListCreateAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return Appointment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UpdateAppointmentStatusView(RetrieveUpdateAPIView):
  
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def update(self, request, *args, **kwargs):
        appointment = self.get_object()
        
        status = request.data.get('status')
        if status not in dict(Appointment.STATUS_CHOICES):
            return Response({"error": "Invalid status."}, status.HTTP_400_BAD_REQUEST)
        
        appointment.status = status
        appointment.save()
        
        return Response(AppointmentSerializer(appointment).data, status.HTTP_200_OK)
