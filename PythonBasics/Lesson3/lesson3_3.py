# Artificial Intelligence
# Igor Ivanov
# Lesson 3. 
# Task3. Function that returns the sum of the largest 2 arguments from 3

def my_func(*args):
    values = list(args)
    values.sort(reverse=True)
    return values[0]+values[1]


def input_num_check(message):
    value = input(message)
    result = value.isdigit()
    if not result:
        print('Incorrect value type. Input number, please')
        value = '1'
    return int(value), result


is_valid = False
while not is_valid:
    term1, is_valid = input_num_check('Input number 1: ')
    if not is_valid:
        continue
    term2, is_valid = input_num_check('Input number 2: ')
    if not is_valid:
        continue
    term3, is_valid = input_num_check('Input number 3: ')
    if not is_valid:
        continue

    print ('Sum of 2 largest numbers is ', my_func(term1, term2, term3))
    is_valid = not input('\nTry more (y-yes, n-no)? ').lower()[0] == 'y'
