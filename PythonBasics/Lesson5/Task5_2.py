# Artificial Intelligence
# Igor Ivanov
# Lesson 5
# Task 2. Calculate number of lines and words in a line at a file

print('File content task2.txt analysis')

with open('task2.txt', 'r') as my_file:
    lines = my_file.read().splitlines()
    print('{0} lines'.format(len(lines)))
    for index, line in enumerate(lines):
        words = len(line.split())
        print(f'{index+1} line has {words} words:')
