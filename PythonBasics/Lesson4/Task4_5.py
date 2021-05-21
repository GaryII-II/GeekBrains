# Artificial Intelligence
# Igor Ivanov
# Lesson 4
# Task 5. Generate list of odd nums and calculate a multiplication of them

from functools import reduce

odd_list = [item for item in range(100, 122) if item % 2 == 0]
print('Multiplication:', reduce(lambda x, y: x*y, odd_list))
