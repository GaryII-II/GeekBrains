# Artificial Intelligence
# Igor Ivanov
# Lesson 6
# Task 1. Traffic light simulation class

class TrafficLight():

    __color = 'green'

    def __init__(self):
        self.__color = 'green'

    def running(self):
        from time import sleep

        print(self.__color)

        sleep(7)
        self.__color = 'yellow'
        print(self.__color)

        sleep(2)
        self.__color = 'red'
        print(self.__color)
        sleep(7)


tl = TrafficLight()
tl.running()
