import pygame

pygame.init()
screen = pygame.display.set_mode((350, 450))

lst = list()


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[None] * width for _ in range(height)]
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
                if self.board[r][i] is None:
                    continue
                if self.board[r][i]:
                    pygame.draw.circle(screen, (255, 0, 0), (self.left + self.cell_size * i + self.cell_size // 2, self.top + self.cell_size * r + self.cell_size // 2), self.cell_size // 2 - 1)
                elif not self.board[r][i]:
                    pygame.draw.circle(screen, (0, 0, 255), (self.left + self.cell_size * i + self.cell_size // 2,
                                                             self.top + self.cell_size * r + self.cell_size // 2), self.cell_size // 2 - 1)

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
        if cell is not None:
            self.on_click(cell)


class Lines(Board):
    def red_ball(self):
        for i in range(len(self.board)):
            for r in range(len(self.board[i])):
                if self.board[i][r] is True:
                    return True, i, r
        return False, -1, -1

    def on_click(self, cell):
        global lst
        check, x, y = self.red_ball()
        if check:
            lst = list()
            if self.has_path(x, y, cell[1], cell[0]) and self.board[cell[1]][cell[0]] is None:
                self.board[cell[1]][cell[0]] = False
                self.board[x][y] = None
                return
        if self.board[cell[1]][cell[0]] is None:
            self.board[cell[1]][cell[0]] = False
        else:
            self.board[cell[1]][cell[0]] = not self.board[cell[1]][cell[0]]

    def has_path(self, x1, y1, x2, y2):
        global lst
        n = 0
        lst1 = list()
        for v in range(-1, 2):
            for k in range(-1, 2):
                x_check, y_check = y1 + k, x1 + v
                if x_check == y1 and y_check == x1:
                    continue
                if x_check < 0 or y_check < 0:
                    continue
                if x_check >= self.width or y_check >= self.height:
                    continue
                if x_check == y2 and y_check == x2:
                    return True
                if self.board[y_check][x_check] is None:
                    lst1.append((y_check, x_check))
                    n += 1
        if lst == list() and n == 0:
            return False
        elif lst != list() and n == 1:
            return False
        else:
            lst.append((x1, y1))
            for i in lst1:
                if i not in lst:
                    if self.has_path(i[0], i[1], x2, y2):
                        return True


board = Lines(5, 7)
board.set_view(50, 50, 50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
