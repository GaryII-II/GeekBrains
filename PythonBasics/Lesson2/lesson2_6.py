# Artificial Intelligence
# Igor Ivanov
# Lesson 2. Task 6

# Building 'Goods' structure from a user input

CAR_MODEL = 'model'
CAR_ENGINE = 'engine'
CAR_PACKAGE = 'package'
CAR_PRICE = 'price'

goods_list = []      # Filled by a user goods list
goods_analysis = {}  # Generated report over the goods

models = set()    # Models range
engines = set()   # Engines range
packages = set()  # Packages range
prices = set()    # Prices range


# Fill values range
def get_values(list_item):

    models.add(list_item[1].get(CAR_MODEL))
    engines.add(list_item[1].get(CAR_ENGINE))
    packages.add(list_item[1].get(CAR_PACKAGE))
    prices.add(list_item[1].get(CAR_PRICE))


# Print price list as a table
def print_price_list():

    if len(goods_list) > 0:
        print('#\tModel\t\tEngine\t\tPackage\tPrice')
        print('=' * 70)

    for line in goods_list:
        print('{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}'.format(line[0],
                                                       line[1].get(CAR_MODEL, 'Unknown'),
                                                       line[1].get(CAR_ENGINE, '0.0'),
                                                       line[1].get(CAR_PACKAGE, 'Unknown'),
                                                       line[1].get(CAR_PRICE, '0')))


print('Fill car shop price list.')

to_add_more = 'y'
index = 0
while to_add_more[0].lower() == 'y':

    model = input('\nInput car model: ').title()
    engine = float(input('Specify engine volume (1.4 / 1.8 / 2.0): '))
    package = input('Specify car package (mini / standard / maxi): ').lower()
    price = int(input('Input expected price (RUB): '))

    goods_list.append((index, {CAR_MODEL: model, CAR_ENGINE: engine, CAR_PACKAGE: package, CAR_PRICE: price}))

    to_add_more = input('\nDo you wand to add more cars (y-yes/n-no)? ')

print_price_list()
print('\nAnalytic report by cars.')

# Create ranges of values
list(map(get_values, goods_list))

# Fill the report
goods_analysis.update({CAR_MODEL: models})
goods_analysis.update({CAR_ENGINE: engines})
goods_analysis.update({CAR_PACKAGE: packages})
goods_analysis.update({CAR_PRICE: prices})

print(goods_analysis)
