from django.db import models
from Tiba import settings

SPECIALITIES = (
    ('DE', 'DENTIST'),
    ('OP', 'OPTICIAN'),
    ('GP', 'GENERAL PRACTITIONER'),
)

class Doctor(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    
    specialization = models.CharField(choices=SPECIALITIES, max_length=100)
    available_days = models.JSONField(default=list)
    available_hours = models.JSONField(default=list)

    def __str__(self):
        return f"Dr. {self.user.get_full_name()} - {self.specialization}"
