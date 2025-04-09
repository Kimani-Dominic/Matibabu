from django.urls import path, include

from doctors.views import DoctorProfileInfo

urlpatterns = [
    path('api/doctor/info', DoctorProfileInfo.as_view(), name="update-doctor-info")
]