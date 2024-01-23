from django.contrib.auth.models import User
from rest_framework import serializers
from users.models import Permissions, UserProfile, MemoryPage, ExtendedMemoryPageInfo, Award, Education, FamilyMember, HobbyInterest, Subscription

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        
        
    

        
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = ['can_add_photos', 'can_add_videos', 'can_add_audio', 'can_add_links', 'can_add_reviews',
                  'can_add_place_of_birth', 'cann_add_place_of_death', 'can_add_spouse',
                  'can_add_nationality', 'can_add_occupation', 'can_add_awards', 'can_add_education',
                  'can_add_family_members', 'can_add_hobbies_interests', 'can_add_life_milestones',
                  'can_add_personal_anecdotes', 'can_add_significant_places']
        
        
        
class SubscriptionSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(read_only=True, many=True)
    class Meta:
        model = Subscription
        fields = ['id', 'name', 'description', 'price', 'max_photos', 'max_videos', 'max_audio', 'max_links', 'permissions']
          
        
class UserProfileSerializer(serializers.ModelSerializer):
    subscription = SubscriptionSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['user', 'subscription']

