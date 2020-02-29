from math import cos, sin, pi, sqrt
import pygame
pygame.init()
screen = pygame.display.set_mode((201, 201))
running = True
clock = pygame.time.Clock()
x0, y0 = 100, 100
lst = [270, 30, 150]


def grad_to_rad(grad):
    return grad/360*pi*2


def mycos(grad):
    return cos(grad_to_rad(grad))


def mysin(grad):
    return sin(grad_to_rad(grad))


def points(grad):
    x1 = x0 + a * cos(grad_to_rad(grad - 15 + 0.5))
    y1 = y0 + a * sin(grad_to_rad(grad - 15 + 0.5))
    x2 = x0 + a * cos(grad_to_rad(grad + 15 + 0.5))
    y2 = y0 + a * sin(grad_to_rad(grad + 15 + 0.5))

    return ((x0, y0), (x1, y1), (x2, y2))


def move(v):
    for i in range(len(lst)):
        lst[i] += v
        if lst[i] >= 360:
            lst[i] -= 360

a = 70
v = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                v -= 1
            if event.button == 3:
                v += 1

    screen.fill((0,0,0))
    pygame.draw.circle(screen, pygame.Color('white'), (x0, y0), 10)
    for i in lst:
        pygame.draw.polygon(screen, pygame.Color('white'), points(i))
    move(v)
    pygame.display.flip()
    clock.tick(50)