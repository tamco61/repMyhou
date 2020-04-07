import os
import sys
from math import sqrt
import pygame
import requests
import random
def coords(text):
    if text != '':
        server = 'https://geocode-maps.yandex.ru/1.x/'
        params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            'geocode': text,
            'format': 'json'
        }
        resp = requests.get(server, params=params).json()
        if resp['response']['GeoObjectCollection']['featureMember'] != []:
            address_ll = resp['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
            address_ll = ','.join(i for i in address_ll.split(' '))
            return address_ll
        return 0
    return 0
n = 0
lst = ['sat', 'map']
ls = ['12', '13']
lst_city = ['Москва', 'Нью-Йорк', 'Санкт-Петербург', 'Уфа']
lst_coord = [coords(i) for i in set(lst_city)]
server = 'https://static-maps.yandex.ru/1.x/'
params = {
    'l': 'map',
    'z': '13',
    'll': '30.25,59.947176',
    'size': '650,450'
}
lst_map = list()
for i in range(len(lst_coord)):
    response = None
    params['ll'] = lst_coord[i]
    z = random.randint(0, 1)
    params['l'] = lst[z]
    params['z'] = ls[z]
    response = requests.get(server, params=params)
    # Запишем полученное изображение в файл.
    map_file = f"map{i}.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    lst_map.append(map_file)
# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((650, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(lst_map[0]), (0, 0))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            n += 1
            if n == len(lst_map):
                n = 0
            screen.fill((0, 0, 0))
            screen.blit(pygame.image.load(lst_map[n]), (0, 0))
            pygame.display.flip()
pygame.quit()
# Удаляем за собой файл с изображением.
for i in lst_map:
    os.remove(i)