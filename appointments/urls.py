from django.urls import path
from .views import *

urlpatterns = [
    path('api/appointments/', CreateAppointmentView.as_view(), name='create_appointment'),
    path('api/appointments/', AppointmentListView.as_view(), name='get_appointments'), 
    path('api/appointments/<int:pk>/update/', UpdateAppointmentStatusView.as_view(), name='update_appointment_status'),
]





