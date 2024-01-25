from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
import json
from .models import MemoryPage

def add_memory_page(request):
    memory_page = MemoryPage.objects.filter(user=request.user).order_by('-id')
    
    return render(request, 'users/user_memory.html',  context={'memory_page': memory_page})



def edit_memory_page(request, memory_page_id):
    memory_page = MemoryPage.objects.get(id=memory_page_id, user=request.user)

    return render(request, 'users/edit_memory.html', {'memory_page': memory_page})
