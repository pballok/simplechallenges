import pygame
import grid_oo
import golbutton

SCREEN_SIZE_X = 860
SCREEN_SIZE_Y = 740
SCREEN_MARGIN = 20
CONTROL_AREA  = 100
BUTTON_WIDTH = CONTROL_AREA
BUTTON_HEIGHT = 20

def drawCells(screen, grid, cell_size):
    for position in range(grid.GRID_SIZE_N * grid.GRID_SIZE_M):
        x = (position % grid.GRID_SIZE_N) * cell_size + SCREEN_MARGIN
        y = (position // grid.GRID_SIZE_N) * cell_size + SCREEN_MARGIN
        color = (255, 255, 255) if grid.isCellAlive(position) else (0, 0, 0)
        pygame.draw.rect(screen, color, (x, y, cell_size, cell_size), 0)

def step(grid):
    pass

def start():
    pass

def stop():
    pass

def exit():
    pass
    
def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_SIZE_X, SCREEN_SIZE_Y))
    done = False

    grid = grid_oo.Grid(100, 100)

    grid.setCell(  2, 1)
    grid.setCell(102, 1)
    grid.setCell(202, 1)
    grid.setCell(201, 1)
    grid.setCell(100, 1)

    grid_size_x = int((SCREEN_SIZE_X - CONTROL_AREA - 3 * SCREEN_MARGIN) / grid.GRID_SIZE_N)
    grid_size_y = int((SCREEN_SIZE_Y - 2 * SCREEN_MARGIN) / grid.GRID_SIZE_M)
    cell_size = min(grid_size_x, grid_size_y)
    grid_width = cell_size * grid.GRID_SIZE_N
    grid_height = cell_size * grid.GRID_SIZE_M

    pygame.draw.rect(screen, (255, 255, 255), (SCREEN_MARGIN, SCREEN_MARGIN, grid_width, grid_height), 1)

    button_top = SCREEN_MARGIN
    step_button  = golbutton.GOLButton((2 * SCREEN_MARGIN + grid_width, button_top, BUTTON_WIDTH, BUTTON_HEIGHT), "Step", step)
    button_top += BUTTON_HEIGHT + SCREEN_MARGIN
    start_button = golbutton.GOLButton((2 * SCREEN_MARGIN + grid_width, button_top, BUTTON_WIDTH, BUTTON_HEIGHT), "Start", start)
    button_top += BUTTON_HEIGHT + 5
    stop_button  = golbutton.GOLButton((2 * SCREEN_MARGIN + grid_width, button_top, BUTTON_WIDTH, BUTTON_HEIGHT), "Stop", stop)
    button_top += BUTTON_HEIGHT + SCREEN_MARGIN
    exit_button  = golbutton.GOLButton((2 * SCREEN_MARGIN + grid_width, button_top, BUTTON_WIDTH, BUTTON_HEIGHT), "Exit", exit)
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            else:
                step_button.check_event(event)
                start_button.check_event(event)
                stop_button.check_event(event)
                exit_button.check_event(event)

        grid.step()
        drawCells(screen, grid, cell_size)

        step_button.draw(screen)
        start_button.draw(screen)
        stop_button.draw(screen)
        exit_button.draw(screen)
            
        pygame.display.flip()

main()