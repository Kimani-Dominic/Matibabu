from django.db import models

from Auth.models import User
from appointments.models import Appointment
from patients.models import Patient

user = User

class MedicalRecord(models.Model):
    patient = models.ForeignKey(user, on_delete=models.CASCADE, related_name='medical_records')
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='appointments')
    diagnosis = models.TextField()
    treatment= models.TextField()
    prescription = models.TextField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Medical Record for {self.patient.username} - {self.appointment.appointment_time}"
