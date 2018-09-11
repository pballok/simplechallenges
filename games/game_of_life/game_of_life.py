import pygame
import grid_oo
import golbutton

GRID_SIZE_X = 100
GRID_SIZE_Y = 100

SCREEN_SIZE_X = 860
SCREEN_SIZE_Y = 740
SCREEN_MARGIN = 20
CONTROL_AREA  = 100
BUTTON_WIDTH = CONTROL_AREA
BUTTON_HEIGHT = 20

class Game:

    def __init__(self, screen, cell_size):

        self.screen = screen
        self.cell_size = cell_size

        self.exiting = False
        self.playing = False
        self.grid = grid_oo.Grid(GRID_SIZE_X, GRID_SIZE_Y)

        self.grid.setCell(  2, 1)
        self.grid.setCell(102, 1)
        self.grid.setCell(202, 1)
        self.grid.setCell(201, 1)
        self.grid.setCell(100, 1)
        self.drawCells()

    def drawCells(self):
        for position in range(self.grid.GRID_SIZE_N * self.grid.GRID_SIZE_M):
            x = (position % self.grid.GRID_SIZE_N) * self.cell_size + SCREEN_MARGIN
            y = (position // self.grid.GRID_SIZE_N) * self.cell_size + SCREEN_MARGIN
            color = (255, 255, 255) if self.grid.isCellAlive(position) else (0, 0, 0)
            pygame.draw.rect(self.screen, color, (x, y, self.cell_size, self.cell_size), 0)

    def step(self):
        self.grid.step()
        self.drawCells()

    def start(self):
        self.playing = True

    def stop(self):
        self.playing = False

    def exit(self):
        self.exiting = True

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_SIZE_X, SCREEN_SIZE_Y))

    grid_size_x = int((SCREEN_SIZE_X - CONTROL_AREA - 3 * SCREEN_MARGIN) / GRID_SIZE_X)
    grid_size_y = int((SCREEN_SIZE_Y - 2 * SCREEN_MARGIN) / GRID_SIZE_Y)
    cell_size = min(grid_size_x, grid_size_y)
    grid_width = cell_size * GRID_SIZE_X
    grid_height = cell_size * GRID_SIZE_Y

    pygame.draw.rect(screen, (255, 255, 255), (SCREEN_MARGIN, SCREEN_MARGIN, grid_width, grid_height), 1)

    game = Game(screen, cell_size)

    button_top = SCREEN_MARGIN
    step_button  = golbutton.GOLButton((2 * SCREEN_MARGIN + grid_width, button_top, BUTTON_WIDTH, BUTTON_HEIGHT), "Step", game.step)
    button_top += BUTTON_HEIGHT + SCREEN_MARGIN
    start_button = golbutton.GOLButton((2 * SCREEN_MARGIN + grid_width, button_top, BUTTON_WIDTH, BUTTON_HEIGHT), "Start", game.start)
    button_top += BUTTON_HEIGHT + 5
    stop_button  = golbutton.GOLButton((2 * SCREEN_MARGIN + grid_width, button_top, BUTTON_WIDTH, BUTTON_HEIGHT), "Stop", game.stop)
    button_top += BUTTON_HEIGHT + SCREEN_MARGIN
    exit_button  = golbutton.GOLButton((2 * SCREEN_MARGIN + grid_width, button_top, BUTTON_WIDTH, BUTTON_HEIGHT), "Exit", game.exit)

    while not game.exiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.exit()
            else:
                step_button.check_event(event)
                start_button.check_event(event)
                stop_button.check_event(event)
                exit_button.check_event(event)

        if game.playing:
            game.step()

        step_button.draw(screen)
        start_button.draw(screen)
        stop_button.draw(screen)
        exit_button.draw(screen)

        pygame.display.flip()

main()
