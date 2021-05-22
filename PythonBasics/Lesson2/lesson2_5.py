# Artificial Intelligence
# Igor Ivanov
# Lesson 2. Task 5

# Rating structure implementation from natural numbers

natural_numbers = [12, 10, 10, 7, 6, 6, 5, 4, 1]

given_num = int(input('Input any number: '))

print('Initial rating:', natural_numbers)

# Find the position to insert
index = len(natural_numbers)+1
if given_num > natural_numbers[-1]:
    for index, number in enumerate(natural_numbers):
        if number < given_num:
            break

natural_numbers.insert(index, given_num)

print('Updated rating:', natural_numbers)
print('Number was inserted to pos ', )
