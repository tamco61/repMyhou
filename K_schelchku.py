import pygame

pygame.init()

screen = pygame.display.set_mode((501, 501))

v = 1
x, y = 0, 0
x0, y0 = 250, 250
running = True
draw = False
clock = pygame.time.Clock()
pygame.draw.circle(screen, pygame.Color('red'), (x0, y0), 20)
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			x, y = event.pos
			draw = True
	if draw:
		if x0 == x and y0 == y:
			draw = False
		elif y > y0:
			y0 += v
			if x > x0:
				x0 += v
			else:
				x0 -= v
		elif y < y0:
			y0 -= v
			if x > x0:
				x0 += v
			else:
				x0 -= v
		elif y == y0:
			if x > x0:
				x0 += v
			else:
				x0 -= v
		screen.fill((0, 0, 0))
		pygame.draw.circle(screen, pygame.Color('red'), (x0, y0), 20)
	clock.tick(120)
	pygame.display.flip()
