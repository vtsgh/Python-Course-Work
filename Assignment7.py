# Vangjel Thomaj CMIS 102 7383 may 2nd 2022

# variables that store our data, food and gas are empty arrays
# x is used for our while loop we have at 0
food = []
gas = []
x = 0

# these are our prompts for people going on vacation and days spent on vacation
people = int(input('How many people are going on this vacation? '))
days = int(input('How many days is this vacation going to last? '))

# while loop that loops until x is greater than number of days
# we add +1 to x every loop
# user gets prompted for cost of food and gas for the day
# Values entered get appended into their respective arrays
while x < days:
    x += 1
    dailyFood = float(input('How much did it cost for food today '))
    food.append(dailyFood)
    dailyGas = float(input('How much did it cost for gas today '))
    gas.append(dailyGas)

# print statement for summary of cost for each day
print('\nThis is how much you spent on food each day', food)
print('\nThis is how much you spent on food each day', gas)

# sum of values for food and gas inside their own arrays
totalFood = sum(food)
print('\nTogether everyone spent', totalFood, 'dollars on food this vacation')
totalGas = sum(gas)
print('\nTogether everyone spent', totalGas, 'dollars on gas this vacation')

# total cost of food and gas outside of their own arrays
totalcost = totalFood + totalGas
print('\nTogether everyone spent a total of', totalcost, 'dollars on this vacation')

# total cost of vacation divided by people going on the trip
split = totalcost / people
print('\nSplit evenly between', people, 'people, the cost per person is', split, 'dollars on this vacation')