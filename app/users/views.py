from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
import json
from django.views import View

from .models import MemoryPage


class ManageMemoryPageView(View):
    def get(self, request: HttpRequest):
        user = request.user
        # memory_page = MemoryPage.objects.filter(user=user).order_by('-id')
        return render(request, 'users/create_memory.html')

    def post(self, request: HttpRequest):
        family_members = request.POST.get('family_members')
        print(family_members)
        awards = request.POST.get('awards')
        print(awards)
        
        # awards  = self._parse_data_to_json(request, type = 'awards')
        return HttpResponse("ok")
    
    def  _parse_data_to_json(self, request: HttpRequest, type: str):
        awards_data = {}
        for key, value in request.POST.items():
            # Разбить ключ на части
            parts = key.split('[')
            if parts[0] == 'awards':
                # Извлечь индекс и поле
                index = int(parts[1].split(']')[0])
                field = parts[2].strip('][')
                # Создать новую запись, если ее еще нет
                if index not in awards_data:
                    awards_data[index] = {}
                # Добавить данные в соответствующую запись
                awards_data[index][field] = value

        # Удалить пустые записи
        awards_data = {k: v for k, v in awards_data.items() if any(v.values())}

        # Конвертировать в JSON
        awards_json = json.dumps(list(awards_data.values()))

        return awards_json

def add_memory_page(request: HttpRequest):
    # memory_page = MemoryPage.objects.filter(user=request.user).order_by('-id')
    
    return render(request, 'users/create_memory.html',  )



def edit_memory_page(request: HttpRequest, memory_page_id: int):
    # memory_page = MemoryPage.objects.get(id=memory_page_id, user=request.user)

    return render(request, 'users/edit_memory.html')
