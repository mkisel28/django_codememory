from django.utils.deprecation import MiddlewareMixin
from users.models import Subscription
import logging

logger = logging.getLogger(__name__)
class SubscriptionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user = request.user
        if user.is_authenticated:
            try:
                subscription = Subscription.objects.get(user=user)
                request.user_subscription_type = subscription.subscription_type
            except Subscription.DoesNotExist:
                request.user_subscription_type = 'none'
            except Exception as e:
                logger.error(e, exc_info=True)
                request.user_subscription_type = 'none'
        else:
            request.user_subscription_type = 'none'
