# Artificial Intelligence
# Igor Ivanov
# Lesson 6
# Task 3. Inheritance Worker -> Position


class Worker:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 20000, "bonus": 5000}

    def _set_income(self, wage, bonus):
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super(Position, self).__init__(name, surname, position)
        super(Position, self)._set_income(wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        income = self._income['wage'] + self._income['bonus']
        return income


janitor = Position('John', 'Smith', 'janitor', 10000, 1000)
print('Full name is', janitor.get_full_name())
print('Income = ', janitor.get_total_income(), 'for position', janitor.position)
janitor.name = 'Arthur'
print('Full name is', janitor.get_full_name())

waitress = Position('Maria', 'Gomez', 'waitress', 20000, 3000)
print('Full name is', waitress.get_full_name())
print('Income = ', waitress.get_total_income(), 'for position', waitress.position)
