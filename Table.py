from Nodo import Nodo
class Table:
    def __init__(self, width, height):
        self.width  = width
        self.height = height
        self.board = []
        self.build(height, width)

    def build(self, rows, width):
        grid = []
        gap = width // rows
        for i in range(rows):
            grid.append([])
            for j in range(rows):
                nodo = Nodo(i, j, gap, rows)
                grid[i].append(nodo)
        
        self.board = grid

    def get_nodo(self, row, width):
        return self.board[row][width]