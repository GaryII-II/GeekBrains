# Artificial Intelligence
# Igor Ivanov
# Lesson 5
# Task 4. Translate English sentences from file task4_in.txt to Russian at file task4_out.txt

print('Read task4_in.txt and write to task4_out.txt')

dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('task4_in.txt', 'r') as in_file:
    with open('task4_out.txt', 'w', encoding='utf-8') as out_file:
        for line in in_file:
            tag = line.split()[0]
            out_file.write(line.replace(tag, dictionary[tag]))
