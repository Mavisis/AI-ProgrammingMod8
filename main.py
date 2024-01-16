import pygame
import sys
import math

from GameEnvironment import ConnectFour
from GameGrapgics import ConnectFourGUI


def main():
    connect_four_game = ConnectFour(6,7)
    gui = ConnectFourGUI(connect_four_game, 100)

    while not gui.connect_four.game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(gui.screen, gui.BLACK, (0, 0, gui.width, gui.SQUARESIZE))
                posx = event.pos[0]
                if gui.connect_four.turn == 0:
                    pygame.draw.circle(gui.screen, gui.RED, (posx, int(gui.SQUARESIZE / 2)), gui.RADIUS)
                else:
                    pygame.draw.circle(gui.screen, gui.YELLOW, (posx, int(gui.SQUARESIZE / 2)), gui.RADIUS)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(gui.screen, gui.BLACK, (0, 0, gui.width, gui.SQUARESIZE))
                posx = event.pos[0]
                col = int(math.floor(posx / gui.SQUARESIZE))

                if gui.connect_four.is_valid_location(col):
                    row = gui.connect_four.get_next_open_row(col)
                    gui.connect_four.drop_piece(row, col, gui.connect_four.turn + 1)

                    if gui.connect_four.winning_move(gui.connect_four.turn + 1):
                        gui.display_winner(gui.connect_four.turn + 1)
                        gui.connect_four.game_over = True

                gui.connect_four.print_board()
                gui.draw_board()

                gui.connect_four.turn += 1
                gui.connect_four.turn = gui.connect_four.turn % 2

                if gui.connect_four.game_over:
                    pygame.time.wait(3000)


if __name__ == "__main__":
    pygame.init()
    main()