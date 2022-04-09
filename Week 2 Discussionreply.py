#Program to calculate how many meals eaten in a year
#Greet the user
print('Hello. \nPlease follow the prompts to find how many meals you eat in a year.')
#Prompt for number of days the user eats breakfast, lunch and dinner in a week
breakfast = eval (input('How many days on average do you eat breakfast in a week? '))
lunch = eval (input('How about lunch? '))
dinner = eval (input('and how many times a week do you eat dinner? '))
snack = eval(input('Finally,how many times a week do you eat snacks? '))
#Compute and display average total meals a year
year = 52 #weeks in a year
meals_annualy = (breakfast + lunch + dinner + snack) * year
print('Your average yearly meal consumption is:', meals_annualy, 'meals.')
