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
print('Введите адрес школы:')
street_school = input()
print('Введите адрес дома:')
street_home = input()
server = 'https://geocode-maps.yandex.ru/1.x/'
params_home = {
    'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
    'geocode': street_home,
    'format': 'json'
}
params_school = {
    'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
    'geocode': street_school,
    'format': 'json'
}
home = requests.get(server, params=params_home).json()
school = requests.get(server, params=params_school).json()
pos_home = [float(i) for i in home['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')]
pos_school = [float(i) for i in school['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')]
print(f'От дома до школы {round(lonlat_distance(pos_home, pos_school))}м.')