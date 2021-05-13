# Artificial Intelligence
# Igor Ivanov
# Lesson 3. 
# Task5. Runtime sum of the numbers from a user input

def func_input_line():
    line_sum = 0
    line = input('>> ')

    q_index = line.upper().find('Q')
    stop = q_index != -1

    if q_index != -1:
        numbers = line[:q_index:].split()
    else:
        numbers = line.split()

    for num in numbers:
        line_sum += int(num)

    return line_sum, stop


print('Start space-separated numbers input. Use Q to quit:')

to_stop = False
full_sum = 0
while not to_stop:
    _sum, to_stop = func_input_line()
    full_sum += _sum

print('Sum of the input is ', full_sum)
