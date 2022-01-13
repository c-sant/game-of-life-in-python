class Cell:
    """
    A life cell that can either be alive or dead.
    """

    def __init__(self, board, x: int, y: int, alive: bool = False):
        self.x = x
        self.y = y
        self._alive = alive
        self._board = board
        self._neighbours = self.set_neighbours()

    @property
    def alive(self):
        """Returns True if cell is alive; otherwise, returns False."""
        return self._alive

    def toggle(self):
        """Toggle cell state: dies if alive; becomes alive if dead."""
        self._alive = not self._alive

    def __str__(self):
        return str(int(self._alive))

    def __repr__(self):
        return str(f'[Cell: (x: {self.x}, y: {self.y}, state: {int(self.alive)})]')
    
    def set_neighbours(self):
        """Gets the coordinates for each neighbouring cell."""
        neighbours = []
        for i in range(self.x - 1, self.x + 2):
            for j in range(self.y - 1, self.y + 2):
                if (i, j) == (self.x, self.y): continue
                if i < 0 or j < 0: continue
                if i >= self._board.rows or j >= self._board.cols: continue

                neighbours.append((i, j))
        
        return neighbours
                
    def get_neighbours_states(self):
        """Gets the state each of the neighbouring cell is in currently."""
        return [int(self._board[index].alive) for index in self._neighbours]

    def get_neighbour_population(self):
        """Get total of living neighbour cells."""
        return sum(self.get_neighbours_states())

class Board:
    """The game board that stores all the cells."""

    def __init__(self, rows: int, columns: int):
        self.generate([[0 for col in range(columns)] for row in range(rows)])

    def generate(self, input_board: list):
        """Generates new board out of 2D Python list."""
        self.rows = len(input_board)
        self.cols = len(input_board[0]) if self.rows > 0 else 0
        self._board = []

        for i, row in enumerate(input_board):
            self._board.append([])
            for j, col in enumerate(row):
                if col == 0: self._board[i].append(Cell(self, i, j))
                else: self._board[i].append(Cell(self, i, j, True))

    def __getitem__(self, index):
        row, col = index
        return self._board[row][col]

    def __setitem__(self, index, value):
        row, col = index
        self._board[row][col] = value

    def __str__(self):
        string = []
        for i, row in enumerate(self._board):
            string.append([])
            for col in row:
                string[i].append(str(col))

            string[i] = ' '.join(string[i])

        return '\n'.join(string)

    def update(self):
        """
        Updates the board according to Game of Life rules.
        """
        dying_cells = []
        newborn_cells = []

        for i in range(self.rows):
            for j in range(self.cols):
                if self[i, j].alive:
                    if not (2 <= self[i, j].get_neighbour_population() <= 3): 
                        dying_cells.append(self[i, j])

                elif self[i, j].get_neighbour_population() == 3:
                    newborn_cells.append(self[i, j])


        for cell in dying_cells + newborn_cells:
            cell.toggle()