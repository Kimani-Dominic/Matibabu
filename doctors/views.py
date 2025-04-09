from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework.permissions import IsAuthenticated


from doctors.models import Doctor
from doctors.serializers import DoctorSerializer

# Create your views here.
class DoctorProfileInfo(generics.CreateAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request):
        user = request.user
        
        if not user.is_doctor:
            return Response({"Only users with the role 'Doctor' can register doctor info"}, status.HTTP_403_FORBIDDEN)
        
        
        if Doctor.objects.filter(user=user).exists():
            return Response({"error: You can only update your profile"}, status.HTTP_401_UNAUTHORIZED)
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response({"Doctor's profile has been updated successfully"}, status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    
    