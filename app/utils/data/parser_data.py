import json
from django.http import HttpRequest

def  parse_data_to_json(request: HttpRequest, type: str):
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