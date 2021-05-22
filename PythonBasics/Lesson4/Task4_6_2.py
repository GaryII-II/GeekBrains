# Artificial Intelligence
# Igor Ivanov
# Lesson 4
# Task 6.2. List duplicator with itertools.cycle

from itertools import cycle

#  input_list = []  # Integers list to work with

repeat = 1
init_list = ['January', 'February', 'March', 'April', 'May', 'June']

print('Original list to duplicate: ', init_list)

try:
    repeat = int(input('Input number of repetitions: '))
    if repeat < 1:
        raise AssertionError
except:
    print('Invalid parameter')
    quit()

for item in cycle(init_list):
    if repeat <= 0:
        break
    repeat -= 1
    print(item)
