from django.urls import path 
from . import views
from .views import ManageMemoryPageView

urlpatterns = [
    path('memory-page', ManageMemoryPageView.as_view(), name='api_add_memory_page'),
    # path('memory-page', views.add_memory_page, name='api_add_memory_page'),
    path('memory-page/<int:memory_page_id>', views.edit_memory_page, name='api_edit_memory_page'),
    # path('content/', views.show_content, name='show_content'),
    # path('get-conversation/<int:user_id>/', views.get_conversation, name='get-conversation'),
    #  path('api/get-message/', views.api_get_message, name='api_get_message'),
]
