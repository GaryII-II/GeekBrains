# Artificial Intelligence
# Igor Ivanov
# Lesson 5
# Task 3. Find in a file people with min salary and calculate an average salary

print('File content task3.txt analysis')

sum_salary = 0
max_salary = 20000

with open('task3.txt', 'r') as my_file:
    lines = my_file.read().splitlines()
    print('Totally {0} persons'.format(len(lines)))
    for line in lines:
        words = line.split()
        if len(words) != 2:
            continue
        if words[1].isdigit() and int(words[1]) < max_salary:
            print(line)
        sum_salary += int(words[1])

    print('Average salary = ', sum_salary / len(lines))
