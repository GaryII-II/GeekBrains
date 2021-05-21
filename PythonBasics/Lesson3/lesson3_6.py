# Artificial Intelligence
# Igor Ivanov
# Lesson 3. 
# Task6. 'Titling' input words

def int_func(word):
    return word.lower().capitalize()


line = input('Input space-separated words (better lower case): ')
line_list = line.split()
cap_list = list(map(int_func, line_list))
new_line1 = ' '.join([str(word) for word in cap_list])

print('Capitalized line 1: ', new_line1)

print('Capitalized line 2: ', line.title())
