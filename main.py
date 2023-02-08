import numpy as np
import random
import pygame


null_board = np.zeros((9, 9), dtype=int)


class Solver:
    def __init__(self, arr):
        self.arr = arr

    def search(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr)):
                if self.arr[i, j] == 0:
                    return i, j
        return False

    def test(self, number, x, y):
        for i in range(len(self.arr)):
            if self.arr[x, i] == number:
                return False
        for i in range(len(self.arr)):
            if self.arr[i, y] == number:
                return False
        x_box = (x // 3) * 3
        y_box = (y // 3) * 3
        for i in range(x_box, x_box + 3):
            for j in range(y_box, y_box + 3):
                if self.arr[i, j] == number:
                    return False
        return True

    def solve(self):
        null = self.search()
        if null:
            x, y = null
        else:
            return True

        for i in range(1, 10):
            if self.test(i, x, y):
                self.arr[x, y] = i
                if self.solve():
                    return True
                else:
                    self.arr[x, y] = 0
        return False


class Generate(Solver):

    def generate(self):
        null = self.search()
        if null:
            x, y = null
        else:
            return True

        for i in range(9):
            numbers = random.randint(1, 9)
            if self.test(numbers, x, y):
                self.arr[x, y] = numbers
                if self.generate():
                    return True
                else:
                    self.arr[x, y] = 0
        return False

    def remove(self):
        for i in range(72):
            random_row = np.random.randint(9, size=1)
            row = self.arr[random_row[0], :]
            index = list(range(len(row)))
            random_index = random.sample(index, 1)
            row[random_index] = 0
        return self.arr


play_board = Generate(null_board)
play_board.generate()
play_board.remove()
size = 600
board_color = (251, 247, 245)
font_color = (0, 0, 0)
window = pygame.display.set_mode((size, size))


def highlight():
    position = pygame.mouse.get_pos()
    board_coordinate = tuple(pos // 55 for pos in position)
    start_top = tuple(co * 55 for co in board_coordinate)
    end_top = (start_top[0] + 55, start_top[1])
    start_bottom = (start_top[0], start_top[1] + 55)
    end_bottom = (start_top[0] + 55, start_top[1] + 55)

    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(window, (0, 0, 0), (55 + 55 * i, 55), (55 + 55 * i, 550), 4)
            pygame.draw.line(window, (0, 0, 0), (55, 55 + 55 * i), (550, 55 + 55 * i), 4)
        pygame.draw.line(window, (0, 0, 0), (55 + 55 * i, 55), (55 + 55 * i, 550), 2)
        pygame.draw.line(window, (0, 0, 0), (55, 55 + 55 * i), (550, 55 + 55 * i), 2)
    pygame.display.update()

    for i in range(9):
        for j in range(9):
            if (i + 1, j + 1) == board_coordinate:
                pygame.draw.line(window, (102, 225, 0), start_top, end_top, 2)
                pygame.draw.line(window, (102, 225, 0), start_bottom, end_bottom, 2)
                pygame.draw.line(window, (102, 225, 0), start_top, start_bottom, 2)
                pygame.draw.line(window, (102, 225, 0), end_top, end_bottom, 2)
            pygame.display.update()


def insert_number(number, selected):
    for i in range(10):
        if selected < (1, 1) or selected > (9, 9) or selected == (i, 0) or selected == (i, 10):
            return False
    else:
        font = pygame.font.SysFont('Times New Romans', 30)
        value = font.render(str(number), True, font_color)
        window.blit(value, ((selected[0]) * 55 + 23, (selected[1]) * 55 + 23))
        pygame.display.update()


def erase_number(square):
    pygame.draw.rect(window, board_color, pygame.Rect(square[0] * 55 + 3, square[1] * 55 + 3, 40, 40))
    pygame.display.update()


def visual_solve(board):
    cor = pygame.display.get_surface()
    tools = Solver(board)
    null = tools.search()
    if not null:
        return True
    else:
        x, y = null

    for i in range(1, 10):
        if tools.test(i, x, y):
            board[x, y] = i
            font = pygame.font.SysFont('Times New Romans', 30)
            for j in range(9):
                for k in range(9):
                    if 0 < board[j, k] < 10:
                        value = font.render(str(board[j, k]), True, font_color)
                        window.blit(value, ((k + 1) * 55 + 23, (j + 1) * 55 + 23))
                pygame.display.update()
            if visual_solve(board):
                return True
            else:
                board[x][y] = 0
                if board[x][y] == 0:
                    cor.fill(board_color)
                    for j in range(9):
                        for k in range(9):
                            if 0 < board[j][k] < 10:
                                value = font.render(str(board[j][k]), True, font_color)
                                window.blit(value, ((k + 1) * 55 + 23, (j + 1) * 55 + 23))
                    for j in range(10):
                        if j % 3 == 0:
                            pygame.draw.line(window, (0, 0, 0), (55 + 55 * j, 55), (55 + 55 * j, 550), 4)
                            pygame.draw.line(window, (0, 0, 0), (55, 55 + 55 * j), (550, 55 + 55 * j), 4)
                        pygame.draw.line(window, (0, 0, 0), (55 + 55 * j, 55), (55 + 55 * j, 550), 2)
                        pygame.draw.line(window, (0, 0, 0), (55, 55 + 55 * j), (550, 55 + 55 * j), 2)
                pygame.display.update()


def main():
    global coordinate
    pygame.init()
    pygame.display.set_caption("Sudoku")
    window.fill(board_color)
    font = pygame.font.SysFont('Times New Romans', 30)

    # Draw the starting board and all values inside it.
    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(window, (0, 0, 0), (55 + 55 * i, 55), (55 + 55 * i, 550), 4)
            pygame.draw.line(window, (0, 0, 0), (55, 55 + 55 * i), (550, 55 + 55 * i), 4)
        pygame.draw.line(window, (0, 0, 0), (55 + 55 * i, 55), (55 + 55 * i, 550), 2)
        pygame.draw.line(window, (0, 0, 0), (55, 55 + 55 * i), (550, 55 + 55 * i), 2)
    pygame.display.update()

    for i in range(9):
        for j in range(9):
            if 0 < null_board[i][j] < 10:
                value = font.render(str(null_board[i][j]), True, font_color)
                window.blit(value, ((j + 1) * 55 + 23, (i + 1) * 55 + 23))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                highlight()
                position = pygame.mouse.get_pos()
                coordinate = tuple(pos // 55 for pos in position)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    visual_solve(null_board)
                elif event.key == pygame.K_1:
                    insert_number(1, coordinate)
                elif event.key == pygame.K_2:
                    insert_number(2, coordinate)
                elif event.key == pygame.K_3:
                    insert_number(3, coordinate)
                elif event.key == pygame.K_4:
                    insert_number(4, coordinate)
                elif event.key == pygame.K_5:
                    insert_number(5, coordinate)
                elif event.key == pygame.K_6:
                    insert_number(6, coordinate)
                elif event.key == pygame.K_7:
                    insert_number(7, coordinate)
                elif event.key == pygame.K_8:
                    insert_number(8, coordinate)
                elif event.key == pygame.K_9:
                    insert_number(9, coordinate)
                elif event.key == pygame.K_KP1:
                    insert_number(1, coordinate)
                elif event.key == pygame.K_KP2:
                    insert_number(2, coordinate)
                elif event.key == pygame.K_KP3:
                    insert_number(3, coordinate)
                elif event.key == pygame.K_KP4:
                    insert_number(4, coordinate)
                elif event.key == pygame.K_KP5:
                    insert_number(5, coordinate)
                elif event.key == pygame.K_KP6:
                    insert_number(6, coordinate)
                elif event.key == pygame.K_KP7:
                    insert_number(7, coordinate)
                elif event.key == pygame.K_KP8:
                    insert_number(8, coordinate)
                elif event.key == pygame.K_KP9:
                    insert_number(9, coordinate)
                elif event.key == pygame.K_ESCAPE:
                    erase_number(coordinate)


main()
