import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True
clock = pygame.time.Clock()


class Polygon:
    def __init__(self, tuple):
        self.x, self.y = tuple
        self.d = True

    def draw(self, drawLst):
        global screen
        for i in drawLst:
            x, y = i.get_coords()
            if self.x in range(x - 20, x + 49):
                if self.y + 21 == y:
                    self.d = False
        if self.d:
            self.y += 1
            pygame.draw.polygon(screen, pygame.Color('blue'), ((self.x, self.y), (self.x + 20, self.y), (self.x + 20, self.y + 20), (self.x, self.y + 20)))
        else:
            pygame.draw.polygon(screen, pygame.Color('blue'), ((self.x, self.y), (self.x + 20, self.y), (self.x + 20, self.y + 20), (self.x, self.y + 20)))
        self.d = True


class Platform:
    def __init__(self, tuple):
        self.x, self.y = tuple

    def draw(self):
        global screen
        pygame.draw.polygon(screen, pygame.Color('grey'), ((self.x, self.y), (self.x + 50, self.y), (self.x + 50, self.y + 10), (self.x, self.y + 10)))

    def get_coords(self):
        return self.x, self.y


pol = False

drawLst = list()
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if event.button == 1:
                drawLst.append(Platform(event.pos))
            elif event.button == 3:
                pol = Polygon(event.pos)
        if event.type == pygame.KEYDOWN and pol:
            if event.key == pygame.K_LEFT:
                pol.x -= 10
            if event.key == pygame.K_RIGHT:
                pol.x += 10
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for i in drawLst:
        i.draw()
    if pol:
        pol.draw(drawLst)
    pygame.display.flip()
    clock.tick(50)
