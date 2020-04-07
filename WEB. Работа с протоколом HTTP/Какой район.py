import requests
print('Введите адрес:')
street = input()
server = 'https://geocode-maps.yandex.ru/1.x/'
params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    'geocode': street,
    'format': 'json'
}
resp = requests.get(server, params=params).json()
pos = resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    'geocode': ','.join(i for i in pos.split(' ')),
    'kind': 'district',
    'format': 'json'
}
resp = requests.get(server, params=params).json()
pos = resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['name']
print('Он находится в', pos)