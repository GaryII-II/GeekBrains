# Artificial Intelligence
# Igor Ivanov
# Lesson 2. Task 4

# Print a sentence by words in lines

sentence = input('Input space-separated words: ').split()

# Get the season from a list
for index, word in enumerate(sentence):
    print('{0}: {1}'.format(index, word[0:10]))
