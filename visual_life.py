from life import Cell, Board
from time import sleep
import pygame

# Colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (84, 84, 84)

dead_color = WHITE
alive_color = BLACK

# Dimensions

DIM = 480

# Visual Cell

class VisualCell(Cell):
    """Visual version of the cell."""


    def __init__(self, board, x: int, y: int, alive: bool = False):
        super().__init__(board, x, y, alive)
        self._set_color()


    def toggle(self):
        """Toggles cell state: dies if alive; becomes alive if dead."""
        super().toggle()
        self._set_color()


    def _set_color(self):
        """Changes the color of the cell according to its state."""
        if self._alive: self._color = alive_color
        else: self._color = dead_color

    
    def draw(self, win, width, height):
        self._set_color()
        pygame.draw.rect(win, self._color, (self.x * width, self.y * height, width, height))


class VisualBoard(Board):
    """A visual version of the game board."""


    def __init__(self, win, rows: int, columns: int):
        super().__init__(rows, columns)
        self._win = win

        board_size = self._win.get_width()

        self.cell_height = board_size // self.rows
        self.cell_width = board_size // self.cols
        

    def generate(self, input_board: list):
        """Generates new board out of 2D Python list."""
        self.rows = len(input_board)
        self.cols = len(input_board[0]) if self.rows > 0 else 0
        self._board = []

        for i, row in enumerate(input_board):
            self._board.append([])
            for j, col in enumerate(row):
                if col == 0: self._board[i].append(VisualCell(self, i, j))
                else: self._board[i].append(VisualCell(self, i, j, True))


    def render(self):
        for row in self._board:
            for cell in row:
                cell.draw(self._win, self.cell_height, self.cell_width)

        # grid
        # has to be generated after the cells to appear, hence the two loops

        for i in range(self.rows):
            pygame.draw.line(self._win, GRAY, (0, self.cell_height * i), (DIM, self.cell_height * i))
            for j in range(self.cols):
                pygame.draw.line(self._win, GRAY, (j * self.cell_width, 0), (j * self.cell_width, DIM))


    def get_cell(self, coords):
        """Returns the cell according to its coordinates."""
        x, y = coords
        x = x // self.cell_width
        y = y // self.cell_height

        return self[x, y]

    
    def update(self, speed):
        super().update()
        sleep(speed)

def run():
    global alive_color, dead_color

    win = pygame.display.set_mode((DIM, DIM))
    pygame.display.set_caption("The Game of Life")
    b = VisualBoard(win, 48, 48)

    running = False
    speed = 1

    while True:
        b.render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if pygame.mouse.get_pressed()[0]:
                cell = b.get_cell(pygame.mouse.get_pos())
                if not cell.alive: cell.toggle()

            if pygame.mouse.get_pressed()[2]:
                cell = b.get_cell(pygame.mouse.get_pos())
                if cell.alive: cell.toggle()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    if dead_color == BLACK:
                        dead_color, alive_color = WHITE, BLACK
                        print("alive = black; dead = white")
                    else:
                        dead_color, alive_color = BLACK, WHITE
                        print("alive = white; dead = black")

                if event.key == pygame.K_SPACE:
                    running = not running
                    
                    if running: print("running")
                    else: print("stopping")


                if event.key == pygame.K_r:
                    b = VisualBoard(win, 48, 48)
                    print("board reset")

                if event.key == pygame.K_UP:
                    if speed > 0:
                        speed -= 1
                    print(f'current speed: {speed}')

                if event.key == pygame.K_DOWN:
                    speed += 1
                    print(f'current speed: {speed}')

        if running:
            b.update(speed / 10)


            


        pygame.display.update()

if __name__ == '__main__':
    run()