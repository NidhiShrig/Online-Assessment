from django.urls import path
from .views import RegisterView, UserListView, ProfileView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('token/refresh/', TokenObtainPairView.as_view(), name='token_refresh'),
]   