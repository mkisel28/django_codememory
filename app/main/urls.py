from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='main_index'),

    # path('memory-page', views.add_memory_page, name='api_add_memory_page'),

]