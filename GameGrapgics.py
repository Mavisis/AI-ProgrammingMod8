import pygame
class ConnectFourGUI:
    def __init__(self, connect_four, square_size):
        self.connect_four = connect_four
        self.SQUARESIZE = square_size
        self.width = self.connect_four.COLUMN_COUNT * self.SQUARESIZE
        self.height = (self.connect_four.ROW_COUNT + 1) * self.SQUARESIZE
        self.RADIUS = int(self.SQUARESIZE / 2 - 5)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.myfont = pygame.font.SysFont("monospace", 75)
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.BLUE = (0, 0, 255)

    def draw_board(self):
        for c in range(self.connect_four.COLUMN_COUNT):
            for r in range(self.connect_four.ROW_COUNT):
                pygame.draw.rect(self.screen, self.BLUE, (c * self.SQUARESIZE, r * self.SQUARESIZE + self.SQUARESIZE,self.SQUARESIZE, self.SQUARESIZE))
                pygame.draw.circle(self.screen, self.BLACK,(int(c * self.SQUARESIZE + self.SQUARESIZE / 2),int(r * self.SQUARESIZE + self.SQUARESIZE + self.SQUARESIZE / 2)), self.RADIUS)

        for c in range(self.connect_four.COLUMN_COUNT):
            for r in range(self.connect_four.ROW_COUNT):
                if self.connect_four.board[r][c] == 1:
                    pygame.draw.circle(self.screen, self.RED,
                                       (int(c * self.SQUARESIZE + self.SQUARESIZE / 2), self.height - int(r * self.SQUARESIZE + self.SQUARESIZE / 2)), self.RADIUS)
                elif self.connect_four.board[r][c] == 2:
                    pygame.draw.circle(self.screen, self.YELLOW, (int(c * self.SQUARESIZE + self.SQUARESIZE / 2),self.height - int(r * self.SQUARESIZE + self.SQUARESIZE / 2)), self.RADIUS)
        pygame.display.update()

    def display_winner(self, player):
        label = self.myfont.render(f"Player {player} wins!!", 1, self.RED if player == 1 else self.YELLOW)
        self.screen.blit(label, (40, 10))
        pygame.display.update()
