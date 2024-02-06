import base64
import io
import json
from PIL import Image
from django.http import HttpRequest
import uuid
from django.core.files import File



def get_cropped_image(request: HttpRequest):
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
    