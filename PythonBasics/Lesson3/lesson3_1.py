# Artificial Intelligence
# Igor Ivanov
# Lesson 3. 
# Task1. Function that divides two numbers

def func_div(dividend, divider):
    print(f'Division {dividend} to {divider} equals ', dividend / divider) if divider != 0 else\
        print('Division to 0 is prohibited')


def input_num_check(message):
    value = input(message)
    result = value.isdigit()
    if not result:
        print('Incorrect value type. Input number, please')
        value = '1'
    return int(value), result


is_valid = False
while not is_valid:
    dividend_num, is_valid = input_num_check('Input dividend: ')
    if not is_valid:
        continue
    divider_num, is_valid = input_num_check('Input divider: ')
    if is_valid:
        func_div(dividend_num, divider_num)

    is_valid = not input('Try more (y-yes, n-no)? ').lower()[0] == 'y'
