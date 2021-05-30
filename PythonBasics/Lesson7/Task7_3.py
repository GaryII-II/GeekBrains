# Artificial Intelligence
# Igor Ivanov
# Lesson 7
# Task 3. Class Cell with overridden math operations

class Cell:

    def __init__(self, cell_num):
        self._cell_num = cell_num

    def _type_check(self, obj):
        if type(obj) is not type(self):
            print('Invalid object type')
            return False
        return True

    @property
    def cells_num(self):
        return self._cell_num

    @cells_num.setter
    def cells_num(self, val):
        if val < 0:
            print('Invalid value for a number of cells')
        else:
            self._cell_num = val

    def __add__(self, other):
        if not self._type_check(other):
            return None

        self.cells_num += other.cells_num
        return Cell(self.cells_num)

    def __sub__(self, other):
        if not self._type_check(other):
            return None

        self.cells_num = self.cells_num - other.cells_num
        return Cell(self.cells_num)

    def __mul__(self, other):
        if not self._type_check(other):
            return None

        self.cells_num *= other.cells_num
        return Cell(self.cells_num)

    def __truediv__(self, other):
        if not self._type_check(other):
            return None

        self.cells_num //= other.cells_num
        return Cell(self.cells_num)

    @staticmethod
    def make_order(cell_unit, cells_in_line):

        line = '\n'.rjust(cells_in_line, '*')
        line *= (cell_unit.cells_num // cells_in_line)
        line += '.'.rjust(cell_unit.cells_num % cells_in_line + 1, '*')
        return line


cell1 = Cell(50)
cell2 = Cell(60)

cell1 -= cell2
print(cell1.cells_num)

cell1 += cell2
print(cell1.cells_num)

cell1 *= cell2
print(cell1.cells_num)

cell1 /= cell2
print(cell1.cells_num)

print(cell1.make_order(cell1, 6))
