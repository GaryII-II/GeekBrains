# Artificial Intelligence
# Igor Ivanov
# Lesson 5
# Task 6. Assemble a dict of lessons from a file with lessons

from functools import reduce

# Format: Chemistry: LC=150 PR=20 LB=20
print('Read task6.txt')

out_dict = {}

try:
    with open('task6.txt', 'r', encoding='utf-8-sig') as in_file:
        for line in in_file:
            values = line.split()
            lessons = reduce(lambda x, y: x+y, [int(item.partition('=')[2])
                                                for item in values[1::] if item.partition('=')[2].isdigit()])
            out_dict.update({values[0][0:-1]: lessons})
except:
    import sys
    e = sys.exc_info()
    print('Error: ', e)
    quit()

print(out_dict)
