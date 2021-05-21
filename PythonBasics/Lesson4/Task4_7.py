# Artificial Intelligence
# Igor Ivanov
# Lesson 4
# Task 7. Generator with yield for factorial calculation

#  from itertools import cycle

def fact(n):
    factorial = 1
    for item in range(1, n+1):
        factorial *= item
        yield factorial

try:
    length = int(input('Input length of the numbers array: '))
    if length < 1:
        raise AssertionError
except:
    print('Invalid parameter')
    quit()

for el in fact(length):
    print(el)

