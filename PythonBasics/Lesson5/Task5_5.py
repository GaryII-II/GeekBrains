# Artificial Intelligence
# Igor Ivanov
# Lesson 5
# Task 5. Write numbers and the sum to a file
from random import randint

print('Writing random numbers and the sum to task5.txt')

list_size = int(input('Input list size: '))

with open('task5.txt', 'w+') as my_file:
    my_file.write(' '.join([str(randint(1, 300)) for num in range(list_size)]))

    my_file.seek(0)
    print('Sum of nums = ', sum([int(item) for item in my_file.read().split()]))
