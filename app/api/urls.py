from django.urls import path, include
from .views import CurrentUserView, ExtendedMemoryPageInfoView, FamilyMemberView, MemoryPageView, UserList, PermissionList, UserMemoryPageView
from .views import UserSubscriptionView, UserProfileListView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserList)
router.register('permissions', PermissionList)
router.register('user-profile', UserProfileListView)
router.register('memory-page', MemoryPageView)
router.register('extended-memory-page', ExtendedMemoryPageInfoView)
router.register('family-member', FamilyMemberView)
router.register('user/memory-page', UserMemoryPageView, basename='user-memory-page')
router.register('user/subscription', UserSubscriptionView, basename='user-subscription')
# router.register('user/current', CurrentUserView, basename='current-user')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('user/current/', CurrentUserView.as_view(), name='current-user'),



]
