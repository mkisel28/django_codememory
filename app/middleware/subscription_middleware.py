from django.utils.deprecation import MiddlewareMixin
from users.models import Subscription

class SubscriptionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user = request.user
        if user.is_authenticated:
            try:
                subscription = Subscription.objects.filter(user=user).latest('id')
                request.user_subscription_type = subscription.subscription_type
            except Subscription.DoesNotExist:
                request.user_subscription_type = 'none'
        else:
            request.user_subscription_type = 'none'
