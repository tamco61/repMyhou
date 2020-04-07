import requests
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
print('Введите нужный адрес:')
server = 'https://geocode-maps.yandex.ru/1.x/'
street1 = input()
street2 = 'ул. Академика Королёва, 15, корп. 1, Москва'
params1 = {
    'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
    'geocode': street1,
    'format': 'json'
}
params2 = {
    'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
    'geocode': street2,
    'format': 'json'
}
resp1 = requests.get(server, params=params1).json()
resp2 = requests.get(server, params=params2).json()
pos1 = [float(i) for i in resp1['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')]
pos2 = [float(i) for i in resp2['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')]
l = lonlat_distance(pos1, pos2) / 1000
h1 = 525
h2 = (l/3.6 - math.sqrt(h1)) ** 2
print(f'Минимальная высота приёмной антены = {round(h2)}м.')