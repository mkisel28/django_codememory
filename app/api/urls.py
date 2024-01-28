# from django.urls import path, include
# from .views import CurrentUserView, ExtendedMemoryPageInfoView, FamilyMemberView, UserMemoryPageView, MemoryPageView, SubscriptionsListView, UserList, PermissionList, UserMemoryPagesView
# from .views import UserSubscriptionView, UserProfileListView

# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('users', UserList)
# router.register('subscriptions', SubscriptionsListView)
# router.register('permissions', PermissionList)
# router.register('user-profile', UserProfileListView)
# router.register('memory-page', MemoryPageView)
# router.register('extended-memory-page', ExtendedMemoryPageInfoView)
# router.register('family-member', FamilyMemberView)
# # router.register('user/memory-page', UserMemoryPageView, basename='user-memory-page')
# # router.register('user/subscription', UserSubscriptionView, basename='user-subscription')
# # router.register('user/current', CurrentUserView, basename='current-user')


# urlpatterns = [
#     path('', include(router.urls)),
    
#     path('user/memory-pages/<int:pk>', UserMemoryPageView.as_view(), name='user-memory-page'),
#     path('user/memory-pages', UserMemoryPagesView.as_view(), name='user-memory-pages'),
#     path('user/current', CurrentUserView.as_view(), name='current-user'),
#     path('user/subscription', UserSubscriptionView.as_view(), name='user-subscription'),
# ]




from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserMemoryPageView

router = DefaultRouter()
# router.register('memory-page', UserMemoryPageView, basename='user-memory-page')
# router.register(r'subscriptions', SubscriptionViewSet)
# router.register(r'permissions', PermissionsViewSet)
# router.register(r'userprofiles', UserProfileViewSet)
# router.register(r'memorypages', MemoryPageViewSet)
# router.register(r'extendedmemorypageinfos', ExtendedMemoryPageInfoViewSet)
# router.register(r'awards', AwardViewSet)
# router.register(r'educations', EducationViewSet)
# router.register(r'familymembers', FamilyMemberViewSet)
# router.register(r'hobbyinterests', HobbyInterestViewSet)
# router.register(r'users/memorypage', UserMemoryPageViewSet, basename='user-memory-page')


urlpatterns = [
    path('', include(router.urls)),
    path('user/memory-pages', UserMemoryPageView.as_view(), name='user-memory-page'),
    # path('user-permissions', UserPermissionsView.as_view(), name='user-permissions'),
    # path('user/memory-pages/<int:pk>', UserMemoryPageViewSet.as_view(), name='user-memory-pages'),
    # path('user/memory-pages/', UserMemoryPage.as_view(), name='user-memory-pages'),
]