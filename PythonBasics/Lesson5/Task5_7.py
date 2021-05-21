# Artificial Intelligence
# Igor Ivanov
# Lesson 5
# Task 7. Read firms info, calculate profit data

from sys import exc_info
from json import dump

# Format: Alfa OOO 10000 5000.
print('Read task7_in.txt')

firms = {}
profit = 0
profitables = 0

try:
    with open('task7_in.txt', 'r', encoding='utf-8-sig') as in_file:
        for line in in_file:
            values = line.rstrip('.\n').split()
            diff = int(values[2]) - int(values[3])
            firms.update({values[0]: diff})
            if diff > 0:
                profit += diff
                profitables += 1

    avg_profit = 0 if profitables < 1 else profit / profitables

    with open('task7_out.txt', 'w') as out_file:
        dump([firms, {'average_profit': avg_profit}], out_file)

except:
    e = sys.exc_info()
    print('Error: ', e)
    quit()

