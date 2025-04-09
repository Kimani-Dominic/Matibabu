from django.contrib import admin
from Auth.models import User
from doctors.models import Doctor
from patients.models import Patient

# Register your models here.
@admin.register(User, Patient, Doctor)
class UserAdmin(admin.ModelAdmin):
    pass