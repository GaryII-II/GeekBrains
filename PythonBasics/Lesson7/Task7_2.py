# Artificial Intelligence
# Igor Ivanov
# Lesson 7
# Task 2. Calculate a tissue expenditure for sewing clothes

from abc import ABC, abstractmethod


class Cloth(ABC):

    def __init__(self, name, size, height):
        self.height = height
        self.size = size
        self.name = name

    @abstractmethod
    def tissue_expenditure(self):
        return 0

    @property
    def cloth_name(self):
        return type(self).__name__


class Coat(Cloth):

    @property
    def tissue_expenditure(self):
        return self.size / 6.5 + 0.5


class Suite(Cloth):

    @property
    def tissue_expenditure(self):
        return self.height * 2 + 0.3


coat1 = Coat('Children', size=35, height=135)
coat2 = Coat('Man', size=50, height=189)
suite1 = Suite('Superagent', size=52, height=199)
suite2 = Suite('Receptionist', size=44, height=160)

clothes = [coat1, coat2, suite1, suite2]

total_expenditure = 0
for cloth in clothes:
    total_expenditure += cloth.tissue_expenditure
    print(f'{cloth.name} {cloth.cloth_name} requires {cloth.tissue_expenditure} tissue')

print(f'Total cloth expenditure = {total_expenditure}')
