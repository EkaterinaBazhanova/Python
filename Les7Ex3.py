class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        sumcell = self.cell + other.cell
        return Cell(sumcell)

    def __sub__(self, other):
        subcell = self.cell - other.cell
        if subcell >= 0:
            return Cell(subcell)
        else:
            print(f"Разность количества ячеек первой и второй клеток меньше нуля (клетки отличаются друг от друга на {abs(subcell)} ячеек)!")

    def __mul__(self, other):
        mulcell = self.cell * other.cell
        return Cell(mulcell)

    def __floordiv__(self, other):
        divcell = self.cell // other.cell
        return Cell(divcell)

    def make_order(self, rows):
        od = ""
        for i in range(1, (int(self.cell) // rows) + 1):
            od = od + "*" * rows + "\n"
        od = od + "*" * (self.cell % rows)
        return od

    def __str__(self):
        strcell = str(self.cell)
        return strcell


cell_1 = Cell(28)
cell_2 = Cell(12)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(10))