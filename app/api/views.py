from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import UserSerializer, PermissionSerializer, UserProfileSerializer, SubscriptionSerializer
from users.models import Permissions, UserProfile

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PermissionList(generics.ListAPIView):
    queryset = Permissions.objects.all()
    serializer_class = PermissionSerializer
    
    

class UserSubscriptionView(generics.RetrieveAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        user_profile = UserProfile.objects.get(user=self.request.user)
        return user_profile.subscription
    
    
class UserProfileListView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer