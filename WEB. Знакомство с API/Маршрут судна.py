import os
import sys
import pygame
import requests
# Россия, Санкт-Петербург, Невская губа
# Россия, Санкт-Петербург, Петергоф, Нижний парк
# Россия, Санкт-Петербург, Дворцовая площадь, 2
lst = [29.913479, 59.891714, 30.212564, 59.966514, 30.255084, 59.958165, 30.292420, 59.946800, 30.310187, 59.944949, 30.312397, 59.941434]
response = None
map_request = f'https://static-maps.yandex.ru/1.x/?l=map&ll=30.1,59.947176&spn=0.15,0.16&' \
              f'pt=30.312733,59.940073,comma~29.913845,59.885498,comma&pl={",".join(str(i) for i in lst)}'
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