import pygame
print(pygame.ver)

EMPTY = 0
BLACK = 1
WHITE = 2

black_color = [0, 0, 0]
white_color = [255, 255, 255]

class RenjuBoard(object):
    def __init__(self):
        self._board = [[]] * 15
        self.reset()

    def reset(self):
        for row in range(len(self._board)):
            self._board[row] = [EMPTY] * 15
        
    def move(self, row, col, is_black):
        if self._board[row][col] == EMPTY:
            self._board[row][col] = BLACK if is_black else WHITE
            return True
        return False

    def draw(self, screen):
        for h in range(1, 16):
            pygame.draw.line(screen, black_color, [40, h * 40], [600, h * 40], 1)
            pygame.draw.line(screen, black_color, [h * 40, 40], [h * 40, 600], 1)
        pygame.draw.rect(screen, black_color, [36, 36, 568, 568], 3)
        pygame.draw.circle(screen, black_color, [320, 320], 5, 0)
        pygame.draw.circle(screen, black_color, [480, 160], 3, 0)
        pygame.draw.circle(screen, black_color, [160, 160], 3, 0)
        pygame.draw.circle(screen, black_color, [160, 480], 3, 0)
        pygame.draw.circle(screen, black_color, [480, 480], 3, 0)
        for row in range(len(self._board)):
            for col in range(len(self._board[row])):
                if self._board[row][col] != EMPTY:
                    ccolor = black_color if self._board[row][col] == BLACK else white_color
                    pos = [40 * (col + 1), 40 * (row + 1)]
                    pygame.draw.circle(screen, ccolor, pos, 18, 0)
        
def is_win(board):
    for n in range(15):
        flag = 0
        for b in board._board:
            if b[n] == 1:
                flag += 1
                if flag == 5:
                    print('黑棋胜')
                    return False
            else:
                flag = 0

        flag = 0
        for b in board._board:
            if b[n] == 2:
                flag += 1
                if flag == 5:
                    print('白棋胜')
                    return False
            else:
                flag = 0

        flag = 0
        for b in board._board[n]:
            if b == 1:
                flag += 1
                if flag == 5:
                    print('黑棋胜')
                    return False
            else:
                flag = 0
                flag = 0

        flag = 0
        for b in board._board[n]:
            if b == 2:
                flag += 1
                if flag == 5:
                    print('白棋胜')
                    return False
            else:
                flag = 0

        for x in range(4, 25):
            flag = 0
            for i, b in enumerate(board._board):
                if 14 >= x - i >= 0 and b[x - i] == 1:
                    flag += 1
                    if flag == 5:
                        print('黑棋胜')
                        return False
                else:
                    flag = 0

        for x in range(4, 25):
            flag = 0
            for i, b in enumerate(board._board):
                if 14 >= x - i >= 0 and b[x - i] == 2:
                    flag += 1
                    if flag == 5:
                        print('白棋胜')
                        return False
                else:
                    flag = 0

        for x in range(11, -11, -1):
            flag = 0
            for i, b in enumerate(board._board):
                if 14 >= x + i >= 0 and b[x + i] == 1:
                    flag += 1
                    if flag == 5:
                        print('黑棋胜')
                        return False
                else:
                    flag = 0

        for x in range(11, -11, -1):
            flag = 0
            for i, b in enumerate(board._board):
                if 14 >= x + i >= 0 and b[x + i] == 2:
                    flag += 1
                    if flag == 5:
                        print('白棋胜')
                        return False
                else:
                    flag = 0

    return True

def main():
    board = RenjuBoard()
    is_black = True
    pygame.init()
    pygame.display.set_caption('五子棋')
    screen = pygame.display.set_mode((640, 640))
    screen.fill([125, 95, 24])
    board.draw(screen)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYUP:
                pass

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                row = round((y - 40) / 40)
                col = round((x - 40) / 40)
                if board.move(row, col, is_black):
                    is_black = not is_black
                    screen.fill([125, 95, 24])
                    board.draw(screen)
                    pygame.display.flip()
                    if not is_win(board):
                        running = False
    quit = False
    while not quit:   
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                quit = True

if __name__ == '__main__':
    main()