from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets, mixins
from .serializers import CurrentUserSerializer, ExtendedMemoryPageInfoSerializer, FamilyMemberSerializer, MemoryPageSerializer, UserSerializer, PermissionSerializer, UserProfileSerializer, SubscriptionSerializer
from users.models import ExtendedMemoryPageInfo, FamilyMember, MemoryPage, Permissions, UserProfile

class UserList(viewsets.ModelViewSet):
    """path(users/)

    Args:
        
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PermissionList(viewsets.ModelViewSet):
    queryset = Permissions.objects.all()
    serializer_class = PermissionSerializer
    
    

# class UserSubscriptionView(generics.RetrieveAPIView):
#     serializer_class = SubscriptionSerializer
#     permission_classes = [permissions.IsAuthenticated]
    
#     def get_object(self):
#         user_profile = UserProfile.objects.get(user=self.request.user)
#         return user_profile.subscription
    
    
class UserProfileListView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
    
    
class ExtendedMemoryPageInfoView(viewsets.ModelViewSet):
    queryset = ExtendedMemoryPageInfo.objects.all()
    serializer_class = ExtendedMemoryPageInfoSerializer
    

class MemoryPageView(viewsets.ModelViewSet):
    queryset = MemoryPage.objects.all()
    serializer_class = MemoryPageSerializer
    
class FamilyMemberView(viewsets.ModelViewSet):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer
    
    
    
    
from rest_framework.views import APIView
from rest_framework.response import Response

class UserMemoryPageView(viewsets.ModelViewSet):
    serializer_class = MemoryPageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MemoryPage.objects.filter(user=self.request.user).prefetch_related(
            'extendedmemorypageinfo__family_members',
        )


class UserSubscriptionView(viewsets.GenericViewSet,  mixins.ListModelMixin, mixins.UpdateModelMixin):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return [UserProfile.objects.get(user=self.request.user)]
    
    
class CurrentUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        serializer = CurrentUserSerializer(request.user)
        return Response(serializer.data)
    
    # def list(self, request):
    #     # Метод 'list' используется для обработки GET-запроса без ID
    #     serializer = UserSerializer(request.user)
    #     return Response(serializer.data)
    



