import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True
clock = pygame.time.Clock()


class Polygon:
    def __init__(self, tuple):
        self.x, self.y = tuple
        self.d = True
        self.verh = False

    def draw(self, drawLst):
        global screen
        n = 0
        for i in drawLst:
            x, y = i.get_coords()
            if i.__class__.__name__ == 'Platform':
                if self.x in range(x - 20, x + 49):
                    if self.y + 21 == y:
                        self.d = False
            else:
                if self.x in range(x - 20, x + 10):
                    if self.y in range(y - 70, y):
                        n += 1
        if n > 0:
            self.verh = True
        else:
            self.verh = False
        if self.verh:
            pygame.draw.polygon(screen, pygame.Color('blue'), ((self.x, self.y), (self.x + 20, self.y), (self.x + 20, self.y + 20), (self.x, self.y + 20)))
        else:
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


class Stairs(Platform):
    def draw(self):
        global screen

        pygame.draw.polygon(screen, pygame.Color('red'), ((self.x, self.y), (self.x + 10, self.y), (self.x + 10, self.y - 50), (self.x, self.y - 50)))


pol = False
ctrl_pressed = False
drawLst = list()
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if event.button == 1:
                if not ctrl_pressed:
                    drawLst.append(Platform(event.pos))
                else:
                    drawLst.append(Stairs(event.pos))
            elif event.button == 3:
                pol = Polygon(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == 306:
                ctrl_pressed = True
            if pol:
                if event.key == pygame.K_LEFT:
                    pol.x -= 10
                if event.key == pygame.K_RIGHT:
                    pol.x += 10
                if event.key == pygame.K_UP and pol.verh:
                    pol.y -= 5
                if event.key == pygame.K_DOWN and pol.verh:
                    pol.y += 5
        if event.type == pygame.KEYUP:
            if event.key == 306:
                ctrl_pressed = False
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for i in drawLst:
        i.draw()
    if pol:
        pol.draw(drawLst)
    pygame.display.flip()
    clock.tick(50)