import pygame
from math import sqrt

w, hue = [int(i) for i in input().split(' ')]

pygame.init()

screen = pygame.display.set_mode((300, 300))

colorV = pygame.Color('red')
hsv = colorV.hsva
colorV.hsva = (float(hue), hsv[1], 100, hsv[3])

colorP = pygame.Color('red')
hsv = colorP.hsva
colorP.hsva = (float(hue), hsv[1], 75, hsv[3])

colorZ = pygame.Color('red')
hsv = colorZ.hsva
colorZ.hsva = (float(hue), hsv[1], 50, hsv[3])

pygame.draw.polygon(screen, colorP, [(150 - int(w / 2), 150), (150 + int(w / 2), 150), (150 + int(w / 2), 150 + w), (150 - int(w / 2), 150 + w)])
pygame.draw.polygon(screen, colorV, [(150 - int(w / 2), 150), (150, 150 - int(w / 2)), (150 + w, 150 - int(w / 2)), (150 + int(w / 2), 150)])
pygame.draw.polygon(screen, colorZ, [(150 + w, 150 - int(w / 2)), (150 + int(w / 2), 150), (150 + int(w / 2), 150 + w), (150 + w, 150 - int(w / 2) + w)])

pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()