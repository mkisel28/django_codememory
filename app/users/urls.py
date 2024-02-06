from django.urls import path 
from . import views


urlpatterns = [
    
    path('memory-page', views.add_memory_page, name='user_memory_page'),
    path('create-memory-page', views.create_memory_page, name='api_create_memory_page'),
    path('memory-page/<int:memory_page_id>', views.edit_memory_page, name='memory-page'),
    # path('content/', views.show_content, name='show_content'),
    # path('get-conversation/<int:user_id>/', views.get_conversation, name='get-conversation'),
    #  path('api/get-message/', views.api_get_message, name='api_get_message'),
]
