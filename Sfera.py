import pygame

color_dict = {
    0: 'blue',
    1: 'green',
    2: 'red'
}

pygame.init()

n = int(input())
w = 300
screen = pygame.display.set_mode((w, w))
u = int((300 / n) / 2)
f = 0

for i in range(n):
    pygame.draw.ellipse(screen, pygame.Color(255, 255, 255, 255), (f, 0, 300 - f * 2, 300), 1)
    pygame.draw.ellipse(screen, pygame.Color(255, 255, 255, 255), (0, f, 300, 300 - f * 2), 1)
    f += u

pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()