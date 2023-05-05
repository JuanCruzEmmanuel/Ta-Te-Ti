import pygame
import sys
# Definimos algunas constantes útiles
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# Definimos los colores que usaremos en el juego
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Creamos la clase del juego
class TicTacToe:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tic Tac Toe")
        self.board = [[0 for x in range(BOARD_COLS)] for y in range(BOARD_ROWS)]
        self.player = 1
        self.game_over = False

    def draw_lines(self):
        # Dibujamos las líneas horizontales
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

        # Dibujamos las líneas verticales
        pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    def draw_figures(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] == 1:
                    pygame.draw.circle(self.screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2), int(row * SQUARE_SIZE + SQUARE_SIZE / 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif self.board[row][col] == 2:
                    pygame.draw.line(self.screen, CROSS_COLOR,
                                     (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                     (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                    pygame.draw.line(self.screen, CROSS_COLOR,
                                     (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                     (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                     CROSS_WIDTH)

    def mark_square(self, row, col, player):
        self.board[row][col] = player

    def available_square(self, row, col):
        return self.board[row][col] == 0

    def is_board_full(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] == 0:
                    return False
        return True

    def check_win(self, player):
        # Comprobamos las filas
        for row in range(BOARD_ROWS):
            if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
                self.draw_win_line((0, row), (WIDTH, row))
                return True

        # Comprobamos las columnas
        for col in range(BOARD_COLS):
            if self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player:
                self.draw_win_line((col, 0), (col, HEIGHT))
                return True

        # Comprobamos las diagonales
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            self.draw_win_line((0, 0), (WIDTH, HEIGHT))
            return True

        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            self.draw_win_line((0, HEIGHT), (WIDTH, 0))
            return True

        # Si no se cumple ninguna de las condiciones anteriores, el jugador no ha ganado
        return False

    def draw_win_line(self, start, end):
        pygame.draw.line(self.screen, (255, 215, 0), start, end, WIN_LINE_WIDTH)

    def draw_board(self):
        self.screen.fill(BG_COLOR)
        self.draw_lines()
        self.draw_figures()

    def restart(self):
        self.board = [[0 for x in range(BOARD_COLS)] for y in range(BOARD_ROWS)]
        self.player = 1
        self.game_over = False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]

                    clicked_row = int(mouseY // SQUARE_SIZE)
                    clicked_col = int(mouseX // SQUARE_SIZE)

                    if self.available_square(clicked_row, clicked_col):
                        self.mark_square(clicked_row, clicked_col, self.player)
                        if self.check_win(self.player):
                            self.game_over = True
                        elif self.is_board_full():
                            self.game_over = True
                        else:
                            self.player = self.player % 2 + 1

            self.draw_board()

            if self.game_over:
                pygame.time.wait(500)
                self.restart()

            pygame.display.update()


if __name__ == "__main__":
    TicTacToe().run()