# Artificial Intelligence
# Igor Ivanov
# Lesson 2. Task 2

# List elements exchange in pairs

title = 'Reversed list'
reversed_list = []

user_input = input('Input comma-separated list of elements:').split(',')
print('Input', user_input)

list_size = len(user_input)
print('List size = ', list_size)

if list_size <= 1:
    print(title, user_input)
    pass

i = 0
while i < list_size:
    chunk = user_input[i:i+2:]
    reversed_list.append(chunk[::-1])
    i += 2

print(title, reversed_list)
