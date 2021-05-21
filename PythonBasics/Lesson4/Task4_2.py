# Artificial Intelligence
# Igor Ivanov
# Lesson 4
# Task 2. Extract from a list larger next values
from sys import argv
from random import randint

# Script parameters: number of elements
list_size = 15


def detector(elements):
    prev_item = elements[0]
    for item in elements:
        if item > prev_item:
            yield item
        prev_item = item


if len(argv) != 2 or not argv[1].isdigit():
    print(f'Length has not been specified. Default size = {list_size}')
else:
    list_size = int(argv[1])

our_list = [randint(1, 300) for num in range(list_size)]
print(f'Generated {list_size} elements:\n', our_list)

final_list = [item for item in detector(our_list)]

print(f'Selected {len(final_list)} elements:\n', final_list)