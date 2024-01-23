from django.urls import path 
from . import views


urlpatterns = [
    path('api/add-memory-page/', views.add_memory_page, name='api_add_memory_page'),
    # path('content/', views.show_content, name='show_content'),
    # path('get-conversation/<int:user_id>/', views.get_conversation, name='get-conversation'),
    #  path('api/get-message/', views.api_get_message, name='api_get_message'),
]
