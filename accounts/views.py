from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer, RegisterSerializer, ProfileSerializer
from .permissions import IsAdmin, IsSelfOrAdmin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
    serializer_class = UserSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsSelfOrAdmin]
    serializer_class = ProfileSerializer
    
    def get_object(self):
        return self.request.user