import pyinputplus as pyip

#Made by Andrew Elliott for the python final exam main submission
# store a dictionary of ingredients and their respective prices
optionPrices = {'Wheat' : 2.00,
                'White' : 2.50,
                'Sourdough' : 3.00,
                'Bacon' : 2.00,
                'Sausage' : 2.00,
                'Ham' : 2.00,
                'Combo' : 4.00,
                '1 Egg' : 1.00,
                '2 Eggs' : 2.00,
                '3 Eggs' : 3.00,
                'Hashbrowns' : 2.00,
                'Pancakes' : 3.00,
                'Water' : 0.25,
                'Malk' : 1000.00
                }

customerOrder = [] # a list to store the current order
extras = ['Hashbrowns', 'Pancakes', 'Water', 'Malk']
sandwichTotal = 0.0

# ask the user for bread choice and append to order list
breadChoice = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], 'Please choose your ideal selection of bread:\n', 
lettered=True)
customerOrder.append(breadChoice)

# ask the user for protein choice and append to order list
proteinChoice = pyip.inputMenu(['Bacon', 'Sausage', 'Ham', 'Combo'], 'Please choose your ideal selection of protein, currently if you order all 3 selctions with Combo, you get to save $2:\n', 
lettered=True)
customerOrder.append(proteinChoice)

# ask if the user wants eggs, and if so, record eggs choice
cheeseResponse = pyip.inputYesNo('Would you like Eggs?\n')
if cheeseResponse == 'yes':
    cheeseChoice = pyip.inputMenu(['1 Egg', '2 Eggs', '3 Eggs'], 'Please choose how many eggs you would like, due to supply chain issues we can only offer at most 3 for every meal, we are sorry for the inconviance.:\n', 
lettered=True)
    customerOrder.append(cheeseChoice)
else:
    cheeseChoice = ''

# loop through 'extras' and ask if customer wants each one. If so, append it the order
choice = ''
for i in extras:
    choice = pyip.inputYesNo('Would you like ' + i +'?\n')
    if choice == 'yes':
        customerOrder.append(i)
    else:
        choice = ''

# get the number of sandwiches from the customer
numSandwiches = pyip.inputInt('How many itterations of this meal would you like to order?\n', min=1)

print('\nYour order: ')
# check if the item exists in the options, and get the price for each sandwich
for item in customerOrder:
    if item in optionPrices.keys():
        sandwichTotal += optionPrices.get(item)
        print('\t' + item + ' - $' + str(optionPrices.get(item)))

print('Total for your Meal: $' + str('{:0.2f}'.format(sandwichTotal))) # per sandwhich total
print('Total for your order: (' + str(numSandwiches) + ' Meals @ $' + 
      str('{:0.2f}'.format(sandwichTotal)) + ' each): ')
print('$' + str('{:0.2f}'.format(sandwichTotal * numSandwiches))) # give the total price of sandwiches
