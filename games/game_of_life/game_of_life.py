import pygame
import grid_oo
import golbutton

GRID_SIZE_X = 10
GRID_SIZE_Y = 8

SCREEN_SIZE_X = 860
SCREEN_SIZE_Y = 740
SCREEN_MARGIN = 20
CONTROL_AREA  = 100
BUTTON_WIDTH = CONTROL_AREA
BUTTON_HEIGHT = 20

GRID_WIDTH  = SCREEN_SIZE_X - CONTROL_AREA - 3 * SCREEN_MARGIN
GRID_HEIGHT = SCREEN_SIZE_Y - 2 * SCREEN_MARGIN

class Game:

    def __init__(self, screen):
        self.screen = screen
        self.exiting = False
        self.playing = False
        self.grid = grid_oo.Grid(GRID_SIZE_X, GRID_SIZE_Y)

        cell_size_x = int(GRID_WIDTH / GRID_SIZE_X)
        cell_size_y = int(GRID_HEIGHT / GRID_SIZE_Y)
        self.cell_size = min(cell_size_x, cell_size_y)

    def drawGrid(self):
        first_line_x = SCREEN_MARGIN
        last_line_x = self.cell_size * GRID_SIZE_X + SCREEN_MARGIN

        first_line_y = SCREEN_MARGIN
        last_line_y = self.cell_size * GRID_SIZE_Y + SCREEN_MARGIN

        x_positions = list(range(first_line_x, last_line_x + 1, self.cell_size))
        for x in x_positions:
            pygame.draw.line(self.screen, (128, 128, 128), (x, first_line_y), (x, last_line_y), 1)

        y_positions = list(range(first_line_y, last_line_y + 1, self.cell_size))
        for y in y_positions:
            pygame.draw.line(self.screen, (128, 128, 128), (first_line_x, y), (last_line_x, y), 1)


    def drawCells(self):
        for position in range(self.grid.GRID_SIZE_N * self.grid.GRID_SIZE_M):
            x = (position % self.grid.GRID_SIZE_N) * self.cell_size + SCREEN_MARGIN + 1
            y = (position // self.grid.GRID_SIZE_N) * self.cell_size + SCREEN_MARGIN + 1
            color = (255, 255, 255) if self.grid.isCellAlive(position) else (0, 0, 0)
            pygame.draw.rect(self.screen, color, (x, y, self.cell_size - 2, self.cell_size - 2), 0)

    def step(self):
        self.grid.step()
        self.drawCells()

    def start(self):
        self.playing = True

    def stop(self):
        self.playing = False

    def clear(self):
        self.grid = grid_oo.Grid(GRID_SIZE_X, GRID_SIZE_Y)
        self.drawCells()
        self.playing = False

    def randomize(self):
        for _ in range()

    def load(self):
        pass

    def save(self):
        pass

    def exit(self):
        self.exiting = True

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_SIZE_X, SCREEN_SIZE_Y))

    game = Game(screen)
    if game.cell_size < 3:
        print("Cell size is too small!")
        return

    button_x = 2 * SCREEN_MARGIN + GRID_WIDTH
    button_top = SCREEN_MARGIN
    step_button  = golbutton.GOLButton((button_x, button_top, BUTTON_WIDTH, BUTTON_HEIGHT), "Step", game.step)
    button_top += BUTTON_HEIGHT + 5
    start_button = golbutton.GOLButton((button_x, button_top, BUTTON_WIDTH, BUTTON_HEIGHT), "Start", game.start)
    button_top += BUTTON_HEIGHT + 5
    stop_button  = golbutton.GOLButton((button_x, button_top, BUTTON_WIDTH, BUTTON_HEIGHT), "Stop", game.stop)
    button_top += BUTTON_HEIGHT + SCREEN_MARGIN
    clear_button = golbutton.GOLButton((button_x, button_top, BUTTON_WIDTH, BUTTON_HEIGHT), "Clear", game.clear)
    button_top += BUTTON_HEIGHT + 5
    random_button  = golbutton.GOLButton((button_x, button_top, BUTTON_WIDTH, BUTTON_HEIGHT), "Randomize", game.randomize)
    button_top += BUTTON_HEIGHT + 5
    load_button  = golbutton.GOLButton((button_x, button_top, BUTTON_WIDTH, BUTTON_HEIGHT), "Load", game.load)
    button_top += BUTTON_HEIGHT + 5
    save_button  = golbutton.GOLButton((button_x, button_top, BUTTON_WIDTH, BUTTON_HEIGHT), "Save", game.save)
    button_top += BUTTON_HEIGHT + SCREEN_MARGIN
    exit_button  = golbutton.GOLButton((button_x, button_top, BUTTON_WIDTH, BUTTON_HEIGHT), "Exit", game.exit)

    game.drawGrid()

    while not game.exiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.exit()
            else:
                step_button.check_event(event)
                start_button.check_event(event)
                stop_button.check_event(event)
                clear_button.check_event(event)
                random_button.check_event(event)
                load_button.check_event(event)
                save_button.check_event(event)
                exit_button.check_event(event)

        if game.playing:
            game.step()

        step_button.draw(screen)
        start_button.draw(screen)
        stop_button.draw(screen)
        clear_button.draw(screen)
        random_button.draw(screen)
        load_button.draw(screen)
        save_button.draw(screen)
        exit_button.draw(screen)

        pygame.display.flip()

main()
