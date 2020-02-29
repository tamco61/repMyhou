import pygame
import random

pygame.init()
screen = pygame.display.set_mode((320, 470))


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
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
                pygame.draw.polygon(screen, (255, 255, 255), [(self.left + self.cell_size * i,
                                                                    self.top + self.cell_size * r),
                                                                   (self.left + self.cell_size * (i + 1),
                                                                    self.top + self.cell_size * r),
                                                                   (self.left + self.cell_size * (i + 1),
                                                                    self.top + self.cell_size * (r + 1)),
                                                                   (self.left + self.cell_size * i,
                                                                    self.top + self.cell_size * (r + 1))], 1)
                if self.board[r][i] == 10:
                    pygame.draw.polygon(screen, (255, 0, 0), [(self.left + 1 + self.cell_size * i, self.top + 1 + self.cell_size * r),
                                                                  (self.left - 1 + self.cell_size * (i + 1), self.top + 1 + self.cell_size * r),
                                                                  (self.left - 1 + self.cell_size * (i + 1), self.top - 1 + self.cell_size * (r + 1)),
                                                                  (self.left + 1 + self.cell_size * i, self.top - 1 + self.cell_size * (r + 1))], 0)
                elif self.board[r][i] != -1:
                    textsurface = myfont.render(str(self.board[r][i]), False, (0, 255, 0))
                    screen.blit(textsurface, (self.left + 2 + self.cell_size * i, self.top + 2 + self.cell_size * r))


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
        pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


class Minesweeper(Board):
    def __init__(self, x, y , mine):
        super().__init__(x, y)
        self.mine = mine
        self.random_mine()

    def random_mine(self):
        n = 0
        while True:
            x, y = random.randint(0, len(self.board) - 1), random.randint(0, len(self.board[0]) - 1)
            if self.board[x][y] == -1:
                self.board[x][y] = 10
                n += 1
            if n == 10:
                break

    def on_click(self, cell):
        if self.board[cell[1]][cell[0]] != 10:
            self.open_cell(cell)

    def open_cell(self, cell):
            x, y = cell
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
                    if self.board[y_check][x_check] == 10:
                        n += 1
            self.board[y][x] = n


pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 15)
game = Minesweeper(10, 15, 10)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.get_click(event.pos)
    screen.fill((0, 0, 0))
    game.render()
    pygame.display.flip()