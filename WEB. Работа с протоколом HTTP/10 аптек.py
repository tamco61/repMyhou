import sys
from io import BytesIO
import requests
from PIL import Image
import math
# Определяем функцию, считающую расстояние между двумя точками, заданными координатами
def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000 # 111 километров в метрах
    a_lon, a_lat = a
    b_lon, b_lat = b
    # Берем среднюю по широте точку и считаем коэффициент для нее.
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)
    # Вычисляем смещения в метрах по вертикали и горизонтали.
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor
    # Вычисляем расстояние между точками.
    distance = math.sqrt(dx * dx + dy * dy)
    return distance
print('Введите адрес:')
street = input()
server = 'https://geocode-maps.yandex.ru/1.x/'
params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    'geocode': street,
    'format': 'json'
}
resp = requests.get(server, params=params).json()
address_ll = resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
address_ll = ','.join(i for i in address_ll.split(' '))
#  Поиск организации
search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": address_ll
}
response = requests.get(search_api_server, params=search_params)
lst = []
json_response = response.json()
for i in range(10):
    organization = json_response["features"][i]
    # Название организации.
    org_name = organization["properties"]["CompanyMetaData"]["name"]
    point = organization["geometry"]["coordinates"]
    org_point = "{0},{1}".format(point[0], point[1])
    organization["properties"]["CompanyMetaData"]['Hours']['text'] = organization["properties"]["CompanyMetaData"]['Hours'].get('text', '')
    time = organization["properties"]["CompanyMetaData"]['Hours']['text']
    if 'круглосуточно' in time:
        lst.append(f'{org_point},pm2dgl')
    elif '' == time:
        lst.append(f'{org_point},pm2qrl')
    else:
        lst.append(f'{org_point},pm2bll')
# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
    # позиционируем карту центром на наш исходный адрес
    "l": "map",
    # добавим точку, чтобы указать найденную аптеку
    "pt": '~'.join(i for i in lst)
}
map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)
Image.open(BytesIO(
    response.content)).show()