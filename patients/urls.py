from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register(r'patients', PatientViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', PatientViewSet.as_view({'get': 'list'}), name='patients'),
    path('api/register-patient-info/', RegisterPatientInfo.as_view(), name="register-patient"),
    path('api/update-patient-info/', UpdatePatientInfo.as_view(), name="update-patient"),
]