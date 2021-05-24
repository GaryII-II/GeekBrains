# Artificial Intelligence
# Igor Ivanov
# Lesson 5
# Task 1. Write user input to a file.

print('Input lines to write to task1.txt')

with open('task1.txt', 'w+') as my_file:
    line = 'start'
    while line != '':
        line = input()
        my_file.write(line+'\n')

    my_file.seek(0)
    content = my_file.read()
    print('File content:\n', content)
