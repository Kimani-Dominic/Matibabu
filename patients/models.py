from django.db import models
from Auth.models import User
from Tiba import settings

# Create your models here.
class Patient(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    dob = models.DateField()
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    insurance_provider = models.CharField(max_length=255, default="SHA")
    insurance_number = models.CharField(max_length=100, default="321_qwerty")
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Patient {self.user.username}"
