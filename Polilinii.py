import pygame

pygame.init()
screen = pygame.display.set_mode((350, 450))

lst = list()
num = -1
clock = pygame.time.Clock()
lmt = list()
k = -1

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
        self.n = 0

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size


    def render(self):
        global screen, num
        if self.n == 0:
            pass
        if num > 0:
            self.chet()
            num -= 1
        elif num == 0:
            num = -1

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
    
    def chet(self):
        global num, lst
        if num == -1:
            num = len(lst) - 1
        x1, y1 = lst[num]
        x2, y2 = lst[num - 1]
        self.board[x1][y1] = None
        self.board[x2][y2] = True
        if num - 1 == 0:
            self.board[x2][y2] = False

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
            boolean, ls = self.has_path(x, y, cell[1], cell[0])
            if boolean and (self.board[cell[1]][cell[0]] is None or (cell[1] == x and cell[0] == y)):
                lst = list(ls)
                self.chet()
                return
        else:
            if self.board[cell[1]][cell[0]] is None:
                self.board[cell[1]][cell[0]] = False
            else:
                self.board[cell[1]][cell[0]] = not self.board[cell[1]][cell[0]]

    def has_path(self, x1, y1, x2, y2):
        global lst, k, lmt
        v = k + 1
        k += 1
        n = 0
        lst_next_path = list()
        if x1 > x2:
            x_f, y_f, q_f = -1, 2, 1
        else:
            x_f, y_f, q_f = 1, -2, -1
        if y1 > y2:
            x_s, y_s, q_s = -1, 2, 1
        else:
            x_s, y_s, q_s = 1, -2, -1

        for i in range(x_f, y_f, q_f):
            for r in range(x_s, y_s, q_s):
                if i in [-1, 1] and r in [-1, 1]:
                    continue
                if x1 + i == x2 and y1 + r == y2:
                    return True, [(x2, y2), (x1, y1)]
                if i == 0 and r == 0:
                    continue
                if x1 + i not in range(0, self.height) or y1 + r not in range(0, self.width):
                    continue
                if self.board[x1 + i][y1 + r] is None:
                    n += 1
                    lst_next_path.append((x1 + i, y1 + r))
        for i in lst_next_path:
            if i not in lst:
                lst.append(i)
                boolean, ls = self.has_path(i[0], i[1], x2, y2)
                if boolean:
                    ls.append((x1, y1))
                    lmt.append(ls)
                    if v != 0:
                        return True, ls
        if lmt != list() and v == 0:
            gg = 0
            for i in lmt:
                if gg == 0:
                    gg = i
                if len(gg) > len(i):
                    gg = i
            k = -1
            lmt = list()
            return True, gg
        return False, []


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
    clock.tick(10)