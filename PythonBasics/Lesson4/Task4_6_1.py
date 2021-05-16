# Artificial Intelligence
# Igor Ivanov
# Lesson 4
# Task 6.1. Integers generator

from itertools import count, islice

left = 0
right = 10

try:
    input_raw = input('Input numbers range as XXX-YYY: ').split('-')
    left, right = [int(item) for item in input_raw]
    if left > right:
        raise AssertionError
except:
    print('Invalid parameters')
    quit()

for item in islice(count(left), right-left+1):
    print(item)
