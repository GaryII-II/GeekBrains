# Artificial Intelligence
# Igor Ivanov
# Lesson 2. Task 3

# Season by a month with list and dict

year_list = [['winter', 1, 2, 12], ['spring', 3, 4, 5], ['summer', 6, 7, 8], ['autumn', 9, 10, 11]]
year_dict = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}

month = int(input('Input month number (1 - 12): '))

# Get the season from a list
for season in year_list:
    if month in season:
        print('Season from list is', season[0])
        pass

# Get the season from a dict
for season, months in year_dict.items():
    if month in months:
        print('Season from dict is', season)
        pass
