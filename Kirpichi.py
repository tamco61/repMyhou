import pygame

pygame.init()
w, h = 300, 202
screen = pygame.display.set_mode((w, h))
screen.fill((255, 0, 0))
x = 16
t = True
l = 0
for i in range(12):
    pygame.draw.polygon(screen, pygame.Color('white'), [(0, x), (300, x), (300, x + 1), (0, x + 1)])
    if t:
        v = 31
        for r in range(9):
            pygame.draw.polygon(screen, pygame.Color('white'), [(v, l), (v + 1, l),
                                                                (v + 1, l + 15), (v, l + 15)])
            v += 32
    else:
        v = 16
        for r in range(9):
            pygame.draw.polygon(screen, pygame.Color('white'), [(v, l), (v + 1, l),
                                                                (v + 1, l + 15), (v, l + 15)])
            v += 32
    l += 17
    t = not t
    x += 17
pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()