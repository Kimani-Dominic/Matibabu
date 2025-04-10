from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser): 
    # user roles
    is_patient = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)
    
    def assign_role(self, role):
        """Ensure user can only have one role."""
        if role == "doctor":
            self.is_doctor = True
            self.is_patient = True
        elif role == "patient":
            self.is_patient = True
            self.is_doctor = False
        self.save()
      
   
    groups = models.ManyToManyField(
        "auth.Group", related_name="custom_user_set", blank=False,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="custom_user_permissions", blank=False,
    )
