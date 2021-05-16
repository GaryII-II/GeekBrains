# Artificial Intelligence
# Igor Ivanov
# Lesson 4
# Task 4. Find non-duplicated nums in the list

input_list = []  # Integers list to work with

try:
    input_raw = input('Input comma-separated list of numbers: ').split(',')
    input_list = [int(item) for item in input_raw]
except:
    print('Invalid parameters')
    quit()

print('output list:',  [item for item in input_list if input_list.count(item) == 1])

# print('output list:', output_list)

