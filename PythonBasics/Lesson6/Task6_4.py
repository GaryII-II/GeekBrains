# Artificial Intelligence
# Igor Ivanov
# Lesson 6
# Task 4. Inheritance and class methods overriding

CONST_CIVIL_SPEED_LIMIT = 60


class Car:

    def __init__(self, speed, color, name, is_police):
        self._max_speed = speed  # Car engine speed limit
        self.color = color
        self.name = name
        self._is_police = is_police
        self.__state = 'idle'  # Current car state
        self._speed = 0
        self._car_type = type(self).__name__

    def _show_status(self, state =''):
        if not state:
            st = self.__state
        else:
            st = state
        print(f'{self._car_type} {st}')

    def go(self, speed):
        if speed < self._max_speed:
            self._speed = speed
            self.__state = 'moving'
            self._show_status()
        else:
            self._show_status('ALARM. Engine speed limit! Blocked')

    def stop(self):
        self.__state = 'stopped'
        self._speed = 0
        self._show_status()

    def turn(self, direction):
        self._show_status(f'turned {direction}')

    def show_speed(self):
        self._show_status(f'Speed {self._speed} kmh')


class TownCar(Car):

    def show_speed(self):
        msg = f'Speed {self._speed} kmh.'
        if self._speed > CONST_CIVIL_SPEED_LIMIT:
            msg += ' EXCEEDED SPEED LIMIT!!!'
        self._show_status(msg)


class WorkCar(TownCar):
    pass


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


car1 = TownCar(200, 'red', 'Mazda', False)
car2 = WorkCar(200, 'black', 'Mercedes', False)
car3 = SportCar(400, 'yellow', 'Ferrari', False)
car4 = PoliceCar(240, 'white', 'Ford', True)

car1.go(50)
car2.go(60)
car3.go(90)
car4.go(40)

car1.turn('right')
car2.turn('left')
car3.turn('left')
car4.turn('right')

car1.show_speed()
car2.show_speed()
car3.show_speed()
car4.show_speed()

car1.go(100)
car2.go(100)
car3.go(100)
car4.go(100)

car1.show_speed()
car2.show_speed()
car3.show_speed()
car4.show_speed()

car1.go(200)
car2.go(200)
car3.go(200)
car4.go(200)

car1.show_speed()
car2.show_speed()
car3.show_speed()
car4.show_speed()

car1.stop()
car2.stop()
car3.stop()
car4.stop()

print(f'{car1.name} is {car1.color}')
print(f'{car3.name} is {car3.color}')
car1.color = 'green'
car3.color = 'pink'
print(f'{car1.name} is {car1.color}')
print(f'{car3.name} is {car3.color}')
