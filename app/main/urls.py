from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='main_index'),
    path('memory-page/<int:memory_page_id>', views.memory_page, name='main_memory_page'),
    # path('memory-page', views.add_memory_page, name='api_add_memory_page'),

]