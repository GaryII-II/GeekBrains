# Artificial Intelligence
# Igor Ivanov
# Lesson 6
# Task 5. Overriding methods for Stationery


class Stationery:

    def __init__(self, title):
        self._title = title

    def draw(self):
        print('Drawing has been started...')


class Pen(Stationery):

    def draw(self):
        print(f'{self._title} is starting drawing...')


class Pencil(Stationery):

    def draw(self):
        print(f'{self._title} is drawing...')


class Handle(Stationery):

    def draw(self):
        print(f'{self._title} has already being drawn...')


drawPen = Pen('Pen')
drawPencil = Pencil('Pencil')
drawHandle = Handle('Handle')

drawPen.draw()
drawPencil.draw()
drawHandle.draw()
