# Artificial Intelligence
# Igor Ivanov
# Lesson 4
# Task 1. Salary calculation

from sys import argv

# Script parameters: work_hours, hour_price, bonus

if len(argv) != 4 or (not argv[1].isdigit() or not argv[2].isdigit() or not argv[3].isdigit()):
    print('Invalid parameters. Expected space-separated <work_hours>, <hour_price>, <bonus>')
else:
    print('Salary is ', int(argv[1]) * int(argv[2]) + int(argv[3]), 'RUB')
