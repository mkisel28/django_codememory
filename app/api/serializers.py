# from django.contrib.auth.models import User
# from rest_framework import serializers
# from users.models import Permissions, UserProfile, MemoryPage, ExtendedMemoryPageInfo, Award, Education, FamilyMember, HobbyInterest, Subscription

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'first_name', 'last_name']
        
        
# class SubscriptionListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subscription
#         fields = '__all__'

# class FamilyMemberSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FamilyMember
#         fields = '__all__'



# class ExtendedMemoryPageInfoSerializer(serializers.ModelSerializer):
#     family_members = FamilyMemberSerializer(many =True, required=False)
    
#     class Meta:
#         model = ExtendedMemoryPageInfo
#         fields = "__all__"
                  

# class MemoryPageSerializer(serializers.ModelSerializer):
#     extended_info = ExtendedMemoryPageInfoSerializer(source='extendedmemorypageinfo')


#     class Meta:
#         model = MemoryPage
#         fields = '__all__'
 
 
# class PermissionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Permissions
#         fields = ['subscription', 'can_add_photos', 'can_add_videos', 'can_add_audio', 'can_add_links', 'can_add_reviews',
#                   'can_add_place_of_birth', 'cann_add_place_of_death', 'can_add_spouse',
#                   'can_add_nationality', 'can_add_occupation', 'can_add_awards', 'can_add_education',
#                   'can_add_family_members', 'can_add_hobbies_interests', 'can_add_life_milestones',
#                   'can_add_personal_anecdotes', 'can_add_significant_places']
        
        
        
# class SubscriptionSerializer(serializers.ModelSerializer):
#     permissions = PermissionSerializer(read_only=True, many=True)
#     class Meta:
#         model = Subscription
#         fields = '__all__'
          
        
# class UserProfileSerializer(serializers.ModelSerializer):
#     user = UserSerializer()  
#     subscription = SubscriptionSerializer()  
#     # user_avatar = serializers.ImageField(max_length=None, use_url=True)
#     class Meta:
#         model = UserProfile
#         fields = '__all__'
        
# class CurrentUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'first_name', 'last_name']











#############
from rest_framework import serializers
from users.models import (
    Subscription, Permissions, UserProfile, MemoryPage, 
    ExtendedMemoryPageInfo, Award, Education, FamilyMember, HobbyInterest
)




class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class MemoryPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoryPage
        fields = '__all__'

class ExtendedMemoryPageInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedMemoryPageInfo
        fields = '__all__'

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = '__all__'

class HobbyInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HobbyInterest
        fields = '__all__'
