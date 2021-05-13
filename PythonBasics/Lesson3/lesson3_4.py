# Artificial Intelligence
# Igor Ivanov
# Lesson 3. 
# Task4. Function that elevates floating to integer number

def my_func1(float_num, int_num):
    print(f'Elevate {float_num} to {int_num} = ', float_num**int_num)


def my_func2(float_num, int_num):
    for i in range(1, int_num):
        float_num *= float_num

    print(f'Elevate {float_num} to {int_num} = ', float_num)


f_num = float(input('Input floating number: '))
i_num = int(input('Input integer number: '))

my_func1(f_num, i_num)

my_func2(f_num, i_num)
