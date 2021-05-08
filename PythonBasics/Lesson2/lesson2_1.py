# Artificial Intelligence
# Igor Ivanov
# Lesson 2. Task 1

# List of different data types

data_types = [1, 'two', 3.3, complex(2,3), True, ('one', 'two'), {'title': 'Python lesson', 'version': '3.8'}, {23, 34},
              [111, '111']]

for index, item in enumerate(data_types):
    print(' Item {0} with type {1} has value {2}'.format(index, type(item), item))

