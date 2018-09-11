class Grid:
    GRID_SIZE_N = 0
    GRID_SIZE_M = 0

    def __init__(self, size_n, size_m):
        self.GRID_SIZE_N = size_n
        self.GRID_SIZE_M = size_m
        self.cells = [0] * (self.GRID_SIZE_N * self.GRID_SIZE_M)

    def CountAliveNeighbors(self, position):
        live_neighbors = 0

        top_row = (position < self.GRID_SIZE_N)
        bottom_row = int(position / self.GRID_SIZE_N) == self.GRID_SIZE_M - 1
        left_column = (position % self.GRID_SIZE_N) == 0
        right_column = ((position + 1) % self.GRID_SIZE_N) == 0

        if not top_row:
            live_neighbors += self.cells[position - self.GRID_SIZE_N]
            if not right_column:
                live_neighbors += self.cells[position - self.GRID_SIZE_N + 1]
            if not left_column:
                live_neighbors += self.cells[position - self.GRID_SIZE_N - 1]

        if not bottom_row:
            live_neighbors += self.cells[position + self.GRID_SIZE_N]
            if not right_column:
                live_neighbors += self.cells[position + self.GRID_SIZE_N + 1]
            if not left_column:
                live_neighbors += self.cells[position + self.GRID_SIZE_N - 1]

        if not right_column:
            live_neighbors += self.cells[position + 1]

        if not left_column:
            live_neighbors += self.cells[position - 1]

        return live_neighbors

    def setCell(self, position, alive):
        self.cells[position] = 1 if alive else 0

    def isCellAlive(self, position):
        return True if self.cells[position] == 1 else False

    def step(self):
        new_cells = [0] * (self.GRID_SIZE_N * self.GRID_SIZE_M)

        for i in range(self.GRID_SIZE_N * self.GRID_SIZE_M):
            neighbors = self.CountAliveNeighbors(i)
            if neighbors == 2:
                new_cells[i] = self.cells[i]
            if neighbors == 3:
                new_cells[i] = 1

        self.cells = new_cells



if __name__ == "__main__":
    g = Grid(4, 3)
    assert(g.CountAliveNeighbors(0) == 0)
    assert(g.CountAliveNeighbors(1) == 0)
    assert(g.CountAliveNeighbors(3) == 0)
    assert(g.CountAliveNeighbors(4) == 0)
    assert(g.CountAliveNeighbors(5) == 0)
    assert(g.CountAliveNeighbors(7) == 0)
    assert(g.CountAliveNeighbors(8) == 0)
    assert(g.CountAliveNeighbors(9) == 0)
    assert(g.CountAliveNeighbors(11) == 0)

    for i in range(12):
        g.setCell(i, 1)

    assert(g.CountAliveNeighbors(0) == 3)
    assert(g.CountAliveNeighbors(1) == 5)
    assert(g.CountAliveNeighbors(3) == 3)
    assert(g.CountAliveNeighbors(4) == 5)
    assert(g.CountAliveNeighbors(5) == 8)
    assert(g.CountAliveNeighbors(7) == 5)
    assert(g.CountAliveNeighbors(8) == 3)
    assert(g.CountAliveNeighbors(9) == 5)
    assert(g.CountAliveNeighbors(11) == 3)

    g = Grid(3, 3)
    g.setCell(1, 1)
    g.setCell(4, 1)
    g.setCell(7, 1)

    g.step()

    assert(g.isCellAlive(0) == False)
    assert(g.isCellAlive(1) == False)
    assert(g.isCellAlive(2) == False)
    assert(g.isCellAlive(3) == True)
    assert(g.isCellAlive(4) == True)
    assert(g.isCellAlive(5) == True)
    assert(g.isCellAlive(6) == False)
    assert(g.isCellAlive(7) == False)
    assert(g.isCellAlive(8) == False)

    g.step()

    assert(g.isCellAlive(0) == False)
    assert(g.isCellAlive(1) == True)
    assert(g.isCellAlive(2) == False)
    assert(g.isCellAlive(3) == False)
    assert(g.isCellAlive(4) == True)
    assert(g.isCellAlive(5) == False)
    assert(g.isCellAlive(6) == False)
    assert(g.isCellAlive(7) == True)
    assert(g.isCellAlive(8) == False)

    print("Everything OK")
