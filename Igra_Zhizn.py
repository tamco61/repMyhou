import pygame

pygame.init()
screen = pygame.display.set_mode((620, 620))
clock = pygame.time.Clock()


class Cell:
    def __init__(self, x, y):
        self.life = False
        self.lLife = False
        self.x = x
        self.y = y

    def get_lLife(self):
        return self.lLife

    def set_lLife(self):
        self.lLife = not self.lLife

    def get_life(self):
        return self.life

    def set_life(self):
        self.life = not self.life

    def get_coords(self):
        return self.x, self.y


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[Cell(x, y) for x in range(width)] for y in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        global screen

        for i in range(self.width):
            for r in range(self.height):
                if self.board[r][i].get_life():
                    x, y = i * self.cell_size + self.left + 1, r * self.cell_size + self.top + 1
                    pygame.draw.polygon(screen, pygame.Color('green'), [[x, y], [x + self.cell_size - 2, y],
                                                                        [x + self.cell_size - 2,
                                                                         y + self.cell_size - 2],
                                                                        [x, y + self.cell_size - 2]])
                pygame.draw.polygon(screen, (255, 255, 255, 255), [(self.left + self.cell_size * i,
                                                                    self.top + self.cell_size * r),
                                                                   (self.left + self.cell_size * (i + 1),
                                                                    self.top + self.cell_size * r),
                                                                   (self.left + self.cell_size * (i + 1),
                                                                    self.top + self.cell_size * (r + 1)),
                                                                   (self.left + self.cell_size * i,
                                                                    self.top + self.cell_size * (r + 1))], 1)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        x -= self.left
        y -= self.top
        if x in range(0, self.width * self.cell_size) and y in range(0, self.height * self.cell_size):
            x0 = x // self.cell_size
            y0 = y // self.cell_size
            return x0, y0
        return None

    def on_click(self, cell):
        if cell is not None:
            self.board[cell[1]][cell[0]].set_life()

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


class Life(Board):
    def __init__(self, x, y):
        super().__init__(x, y)

    def low_Life_func(self):
        for i in self.board:
            for r in i:
                if r.get_lLife():
                    r.set_life()
                    r.lLife = False

    def next_move(self):
        for i in self.board:
            for r in i:
                x, y = r.get_coords()
                n = 0
                for v in range(-1, 2):
                    for k in range(-1, 2):
                        x_check, y_check = x + k, y + v
                        if x_check == x and y_check == y:
                            continue
                        if x_check < 0 or y_check < 0:
                            continue
                        if x_check >= self.width or y_check >= self.height:
                            continue
                        if self.board[y_check][x_check].get_life():
                            n += 1
                if r.get_life():
                    if n not in range(2, 4):
                        r.set_lLife()
                else:
                    if n == 3:
                        r.set_lLife()
        self.low_Life_func()


life = Life(30, 30)
life.set_view(10, 10, 20)
running = True
t = False
v = 5
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                life.get_click(event.pos)
            elif event.button == 3:
                t = True
            elif event.button == 4:
                v += 1
            elif event.button == 5:
                v -= 1
                if v < 1:
                    v = 1
        if event.type == pygame.KEYDOWN:
            if event.key == 32:
                t = not t

    if t:
        life.next_move()
    screen.fill((0, 0, 0))
    life.render()
    pygame.display.flip()
    clock.tick(v)