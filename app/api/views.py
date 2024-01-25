# from django.contrib.auth.models import User
# from rest_framework import generics, permissions, viewsets, mixins
# from .serializers import CurrentUserSerializer, ExtendedMemoryPageInfoSerializer, FamilyMemberSerializer, MemoryPageSerializer, SubscriptionListSerializer, UserSerializer, PermissionSerializer, UserProfileSerializer, SubscriptionSerializer
# from users.models import ExtendedMemoryPageInfo, FamilyMember, MemoryPage, Permissions, UserProfile, Subscription

# class UserList(viewsets.ModelViewSet):
#     """path(users/)

#     Args:
        
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class PermissionList(viewsets.ModelViewSet):
#     queryset = Permissions.objects.all()
#     serializer_class = PermissionSerializer
    

# class SubscriptionsListView(viewsets.ModelViewSet):
#     queryset = Subscription.objects.all()
#     serializer_class = SubscriptionListSerializer

# # class UserSubscriptionView(generics.RetrieveAPIView):
# #     serializer_class = SubscriptionSerializer
# #     permission_classes = [permissions.IsAuthenticated]
    
# #     def get_object(self):
# #         user_profile = UserProfile.objects.get(user=self.request.user)
# #         return user_profile.subscription
    
    
# class UserProfileListView(viewsets.ModelViewSet):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
    
    
    
# class ExtendedMemoryPageInfoView(viewsets.ModelViewSet):
#     queryset = ExtendedMemoryPageInfo.objects.all()
#     serializer_class = ExtendedMemoryPageInfoSerializer
    

# class MemoryPageView(viewsets.ModelViewSet):
#     queryset = MemoryPage.objects.all()
#     serializer_class = MemoryPageSerializer
    
# class FamilyMemberView(viewsets.ModelViewSet):
#     queryset = FamilyMember.objects.all()
#     serializer_class = FamilyMemberSerializer
    
    
    
    
# from rest_framework.views import APIView
# from rest_framework.response import Response


# class UserMemoryPageView(APIView):
#     serializer_class = MemoryPageSerializer
#     permission_classes = [permissions.IsAuthenticated]
    
#     def get_object(self, pk):
#         return MemoryPage.objects.get(pk=pk)
    
#     def get(self, request, pk):
#         memory_page = self.get_object(pk)
#         serializer = MemoryPageSerializer(memory_page)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         memory_page = self.get_object(pk)
#         print(request.data)
        
#         # serializer = MemoryPageSerializer(memory_page, data=request.data)
#         # if serializer.is_valid():
#         #     serializer.save(user=request.user)
#         #     return Response(serializer.data)
#         # return Response(serializer.errors)
    
#     def delete(self, request, pk):
#         memory_page = self.get_object(pk)
#         memory_page.delete()
#         return Response(status=204)
    
# class UserMemoryPagesView(APIView):
#     serializer_class = MemoryPageSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         user_profile = UserProfile.objects.get(user=self.request.user)
#         serializer = MemoryPageSerializer(user_profile.user.memory_pages, many=True)
#         return Response(serializer.data)    
    
#     def post(self, request):
#         serializer = MemoryPageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     # def get_queryset(self):
#     #     return MemoryPage.objects.filter(user=self.request.user).prefetch_related(
#     #         'extendedmemorypageinfo__family_members',
#     #     )



# # class UserSubscriptionView(viewsets.GenericViewSet,  mixins.ListModelMixin, mixins.UpdateModelMixin):
# #     serializer_class = UserProfileSerializer
# #     permission_classes = [permissions.IsAuthenticated]
    
# #     def get_queryset(self):
# #         return [UserProfile.objects.get(user=self.request.user)]
    
    
    

# class UserSubscriptionView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
    
#     def get(self, request):
#         user_profile = UserProfile.objects.get(user=self.request.user)
#         serializer = UserProfileSerializer(user_profile)
#         return Response(serializer.data)
    

    
    
    
    
# class CurrentUserView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
    
#     def get(self, request):
#         serializer = CurrentUserSerializer(request.user)
#         return Response(serializer.data)
    



###############################################


from rest_framework import viewsets, status
from users.models import (
    Subscription, Permissions, UserProfile, MemoryPage, 
    ExtendedMemoryPageInfo, Award, Education, FamilyMember, HobbyInterest
)
from .serializers import (
    SubscriptionSerializer, PermissionsSerializer, UserProfileSerializer, 
    MemoryPageSerializer, ExtendedMemoryPageInfoSerializer, AwardSerializer, 
    EducationSerializer, FamilyMemberSerializer, HobbyInterestSerializer
)



from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the memory page.
        return obj.user == request.user

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class PermissionsViewSet(viewsets.ModelViewSet):
    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class MemoryPageViewSet(viewsets.ModelViewSet):
    queryset = MemoryPage.objects.all()
    serializer_class = MemoryPageSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        






class ExtendedMemoryPageInfoViewSet(viewsets.ModelViewSet):
    queryset = ExtendedMemoryPageInfo.objects.all()
    serializer_class = ExtendedMemoryPageInfoSerializer

class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class FamilyMemberViewSet(viewsets.ModelViewSet):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer

class HobbyInterestViewSet(viewsets.ModelViewSet):
    queryset = HobbyInterest.objects.all()
    serializer_class = HobbyInterestSerializer


class UserPermissionsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        subscription = user.profile.subscription
        
        if subscription is None:
            return Response({"error": "Subscription not found"}, status=404)

        try:
            permissions = Permissions.objects.get(subscription=subscription)
            serializer = PermissionsSerializer(permissions)
            return Response(serializer.data)
        except Permissions.DoesNotExist:
            return Response({"error": "Permissions not found"}, status=404)



class UserMemoryPageViewSet(APIView):
    serializer_class = MemoryPageSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    
    
    def get_object(self, pk):
        return MemoryPage.objects.get(pk=pk)
    
    def get(self, request, pk):
        memory_page = self.get_object(pk)
        serializer = MemoryPageSerializer(memory_page)
        return Response(serializer.data)
    
    def post(self, request, pk):
        memory_page = self.get_object(pk)
        
        serializer = MemoryPageSerializer(memory_page, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    

class UserMemoryPage(APIView):
    serializer_class = MemoryPageSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        data = MemoryPage.objects.create(user=request.user)
        serializer = MemoryPageSerializer(data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        user_profile = UserProfile.objects.get(user=self.request.user)
        serializer = MemoryPageSerializer(user_profile.user.memory_pages, many=True)
        return Response(serializer.data)