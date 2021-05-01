# Artificial Intelligence
# Igor Ivanov
# Lesson 1
# 6 tasks


# Try input, output
def task1():
    
    print ("Task 1")

    pizza_name = 'margarita'
    pizza_number = 2
    cola_size = 0.5
    cola_choice = [0.33, 0.5]

    while(True):
        choice = input('Do you like a standard Pizza Set? (Y - yes, N - No): ' )
        if  choice and choice.upper()[0] != 'N':
            break 

        pizza_name = input('Which pizza do you want? ')
        pizza_number = input('How many pizza do you need? ')
        cola_size = input('Choose size of Cola ({} or {}): '.format(*cola_choice) )
     
        if pizza_name != '' and int(pizza_number) > 0 and float(cola_size) in cola_choice:
            break

    print('Please, check your order...')
    print('You have chosen: ', pizza_number, ' of pizza ', pizza_name, ' and ', cola_size, ' of Cola')
    pass


# Try input time and convert
def task2():

    print ("Task 2")

    time_seconds = int(input('Convert seconds to the time. Input seconds number: '))
    
    for_hours = time_seconds // 3600
    for_minutes = (time_seconds % 3600) // 60
    for_seconds = (time_seconds % 3600) % 60
    print('The time is {:02d}:{:02d}:{:02d}'.format( for_hours, for_minutes, for_seconds ) )


# Generate a sum from N
def task3():
 
    print ("Task 3")
   
    while(True):
        user_value = int(input('Magic number. Input any digit from 1 to 9 : '))

        if user_value in range(1,9):
            break
  
    print('Magic sum equals ', user_value + user_value*11 + user_value*111 )
    

# Find the largest digit in the number
def task4():
    print ("Task 4")
    
    number = 0
    while number < 10: 
        number = int(input('Input number more 10: '))

    number_len = len(str(number))
    order = 10 ** (number_len-1)
    max_digit = 0

    while order >= 1: 
        digit = int(number // order)
        number = int(number % order)

        if digit > max_digit:
            max_digit = digit

        order = order / 10
        

    print('Bingo! Maximal digit is ', max_digit)


# Company details
def task5():

    print ("Task 4")

    earnings = int(input('Company earnings (RUB) = '))
    expenses = int(input('Company expenses (RUB) = '))    

    is_profitable = earnings > expenses
    company_result = 'profitable' if is_profitable else 'non profitable'
    print ('The company is ' + company_result)
    
    employees = int(input('Number of company employees = '))

    if is_profitable: 
        print ('Earnings per individual employee = ', (earnings - expenses) / employees, ' RUB' )


#  Training plan for a sportsman
def task6():

    print ("Task 6")

    while(True):
        day_distance = first_day_result = int(input('Input the first day result (km) = '))
        day_distance_goal = int(input('Input daily run distance goal (km) = '))
        if day_distance <= day_distance_goal:
            break

    day = 1
    while day_distance < day_distance_goal:
        day_distance = day_distance + day_distance / 10
        day += 1

    print ('Goal will be achieved on {0} day'.format(day))     


# MAIN TASKS FLOW    
task1()

task2()

task3()

task4()

task5()

task6()
