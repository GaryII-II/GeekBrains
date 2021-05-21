# Artificial Intelligence
# Igor Ivanov
# Lesson 4
# Task 3. Find numbers between 20 and 240 multiple of 20 and 21. Use 1 line

print('Numbers from 20 to 240 multiple of 20 or 21: \n',
      [item for item in range(20, 240) if item % 20 == 0 or item % 21 == 0])
