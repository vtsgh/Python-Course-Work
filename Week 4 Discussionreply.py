#Program to determine the percentage of a paycheck spent on monthly bills

#Prompt user for amount of paycheck and bills
print('Hello. Let\'s find out what percentage of your monthly paycheck is spent on bills.')
pay_check = eval(input('How much is your monthly paycheck? '))
rent = eval(input('How much do you pay for rent? '))
utilities = eval(input('How much do you pay for utilities (gas, water, electric, etc.)? '))
phone = eval(input('How about your cell phone bill? '))
streaming = eval(input('How much for streaming subscriptions? '))
gas = eval(input('How much do you spend on gas per month? '))
groceries = eval(input('How much on groceries? '))
credit = eval(input('How much in total are your monthly credit card bills? '))
other = eval(input('Finally, enter the total amount of any other monthly bills. '))
#added found variable to represent the money found that will reduce the bills for the month
found = eval(input('Today is your lucky day, you found money under the couch, this will help pay your bills! how much money did you find in dollars? '))
all_bills = [rent, utilities, phone, streaming, gas, groceries, credit, other]

#Compute and display percentage spent on bills
#changed the formula to subtract money found from total monthly bill
#this is represented by (sum(all_bills) - found)
def bills(pay_check, all_bills, found):
    percentage = (sum(all_bills) - found) / pay_check * 100
    return print ('This month you spent approximately', round(percentage), 'percent of your monthly income on bills.')


#Call function
#added found to the arguments
bills(pay_check, all_bills, found)
