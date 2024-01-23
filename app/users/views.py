from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def add_memory_page(request):
    a = {
        "1": 121,
        "2":3213
    }
    json_data = json.dumps(a)
    return HttpResponse(json_data)
