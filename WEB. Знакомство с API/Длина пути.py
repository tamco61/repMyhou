import os
import sys
from math import sqrt
import pygame
import requests
# Россия, Санкт-Петербург, Невская губа
# Россия, Санкт-Петербург, Петергоф, Нижний парк
# Россия, Санкт-Петербург, Дворцовая площадь, 2
lst = [29.913479, 59.891714, 30.212564, 59.966514, 30.255084, 59.958165, 30.292420, 59.946800, 30.310187, 59.944949, 30.312397, 59.941434]
def len_s(lst):
    s = 0
    k = 110.37093832995551
    for i in range(0, len(lst) - 3, 2):
        x1 = lst[i]
        x2 = lst[i + 2]
        y1 = lst[i + 1]
        y2 = lst[i + 3]
        x = abs(x1 - x2)
        y = abs(y1 - y2)
        l = sqrt(x ** 2 + y ** 2)
        s += k * l
    print('Длина пути =', str(s)[:str(s).index('.') + 4], 'км')
len_s(lst)
response = None
map_request = f'https://static-maps.yandex.ru/1.x/?l=map&ll=30.1,59.947176&spn=0.15,0.16&' \
              f'pt=30.074467,59.935428,comma&pl={",".join(str(i) for i in lst)}'
response = requests.get(map_request)
if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)
# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)
# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
# Удаляем за собой файл с изображением.
os.remove(map_file)