from django.urls import path, include
from .views import UserList, PermissionList
from .views import UserSubscriptionView, UserProfileListView



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('permissions/', PermissionList.as_view(), name='permission-list'),
    path('user-profile/', UserProfileListView.as_view(), name='user-profile-list'),
    path('user/subscription/', UserSubscriptionView.as_view(), name='user-subscription'),

]