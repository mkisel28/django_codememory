from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
import json
from django.views import View
import os
from django.core.files.base import ContentFile
from PIL import Image
import uuid
from .models import MemoryPage
from django.core.files import File
import base64
import io


class ManageMemoryPageView(View):
    def get(self, request: HttpRequest, memory_page_id: int = None):
        if memory_page_id:
            memory_page = MemoryPage.objects.get(id=memory_page_id, user=request.user)
            if memory_page.awards:
                memory_page.hidden_awards = memory_page.awards
                memory_page.awards = json.loads(memory_page.awards)
            if memory_page.family_composition:
                memory_page.hidden_family_composition = memory_page.family_composition
                memory_page.family_composition = json.loads(memory_page.family_composition)
            return render(request, 'users/edit_memory.html', {'memory_page': memory_page})
        
        else:
            return render(request, 'users/create_memory.html')

    def post(self, request: HttpRequest, memory_page_id: int = None):



        # Использование словаря для упрощения извлечения данных
        form_data = {key: request.POST.get(key) for key in [
            'deceased_first_name', 'deceased_last_name', 'deceased_middle_name', 
            'deceased_birth_date', 'deceased_death_date', 'epitaph', 
            'biography', 'awards', 'family_composition'
        ]}

        image_file = self._upload_cropped_image(request)
        # Обновление существующей страницы памяти
        if memory_page_id:
            try:
                memory_page = MemoryPage.objects.get(id=memory_page_id, user=request.user)
                if image_file:
                    memory_page.avatar = image_file
                for key, value in form_data.items():
                    setattr(memory_page, key, value)
                memory_page.save()
                return HttpResponse("Updated")
            except MemoryPage.DoesNotExist:
                return HttpResponseBadRequest("Memory page does not exist")
        try:
            MemoryPage.objects.create(
                user=request.user, 
                avatar=image_file,
                **form_data
            )
            return HttpResponse("ok")
        except Exception as e:
            # Обработка возможных исключений при создании объекта
            return HttpResponse(f"An error occurred: {e}", status=500)
    
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

    def _upload_cropped_image(self, request: HttpRequest):
    # Получение Data URL изображения из POST данных
        cropped_image_data = request.POST.get('cropped_image_data')
        if cropped_image_data:
            # Извлечение чистого base64 кода и преобразование в бинарный формат
            format, imgstr = cropped_image_data.split(';base64,') 
            ext = format.split('/')[-1] 
            image_data = base64.b64decode(imgstr)

            # Создание изображения из бинарных данных
            image = Image.open(io.BytesIO(image_data))
            width, height = image.size

            # Вычисление новых размеров с максимальной длиной стороны 2000px
            max_length = 2000
            if width > max_length or height > max_length:
                if width > height:
                    new_width = max_length
                    new_height = int(max_length * (height / width))
                else:
                    new_height = max_length
                    new_width = int(max_length * (width / height))

                # Изменение размера изображения
                image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

            # Сохранение измененного изображения в память
            image_io = io.BytesIO()
            image.save(image_io, format=ext.upper())
            image_io.seek(0)

            # Генерация уникального имени файла
            unique_filename = f"{uuid.uuid4()}.jpg"

            # Создание ContentFile и возвращение Django File
            django_file = File(image_io, name=unique_filename)
            return django_file
        else:
            return None
        
        
def add_memory_page(request: HttpRequest):
    # memory_page = MemoryPage.objects.filter(user=request.user).order_by('-id')
    
    return render(request, 'users/create_memory.html',  )



def edit_memory_page(request: HttpRequest, memory_page_id: int):
    memory_page = MemoryPage.objects.get(id=memory_page_id, user=request.user)
    
    if memory_page.awards:
        memory_page.awards = json.loads(memory_page.awards)
    if memory_page.family_composition:
        memory_page.family_composition = json.loads(memory_page.family_composition)


    return render(request, 'users/edit_memory.html', {'memory_page': memory_page})
