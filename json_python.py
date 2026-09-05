import json

json_data = """
{
    "name": "Иван",
    "age": 30,
    "is_student": false,
    "courses": [
        "Python",
        "QA Automation",
        "API Testing"
    ],
    "address": {
        "city": "Москва",
        "zip": "101000"
    }
} """
parser_data = json.loads(json_data)     # парсинг: переводим из обычной строки (str) в словарь (dict), который видится Питоном
#print (parser_data)

data = {'name': 'Мария',
    'age': 25,
    'is_student': True}

json_string = json.dumps (data, indent=4) # сериализация: переводим из словаря (dict) в обычную строку
print (json_string, type (json_string))

with open ("json_example.json", "r", encoding = "utf-8") as file:   # загружаем строку из другого файла, переводим ее в словарь
    read_data = json.load (file)
    print (read_data, type (read_data))

with open ("json_user.json", "w",encoding = "utf-8") as file:
    json.dump (data, file, indent=2, ensure_ascii=False) # откуда берем (data) и куда записываем (файл json_user.json), флаг False убираем кодировку