# Artificial Intelligence
# Igor Ivanov
# Lesson 6
# Task 2. Calculation of asphalt weight in Road class

CONST_ASPHALT_1SM_WEIGHT = 25


class Road:

    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_asphalt_weight(self, depth_cm):

        print('Asphalt weight will be ',  self._length * self._width * CONST_ASPHALT_1SM_WEIGHT * depth_cm, ' kg')


road = Road(5000, 15)
road.get_asphalt_weight(6)
