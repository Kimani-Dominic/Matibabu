from django.urls import path
from .views import MedicalRecordCreateView, PatientMedicalRecordListView

urlpatterns = [
    path('api/records/create/', MedicalRecordCreateView.as_view(), name='create-record'),
    path('api/records/', PatientMedicalRecordListView.as_view(), name='list-records'),
]
