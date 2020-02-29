import pygame

pygame.init()

n = int(input())
w = 155
h = 155
screen = pygame.display.set_mode((w, h))
screen.fill(pygame.Color('yellow'))

x = w // n
t = h // n
y = int(n / 2)

for i in range(t):
    for r in range(x):
        pygame.draw.polygon(screen, pygame.Color('orange'), [(r * n + y, i * n), (r * n, i * n + y),
                                                             (r * n + y, i * n + n), (r * n + n, i * n + y)])

pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()