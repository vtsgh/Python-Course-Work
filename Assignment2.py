#Vangjel Thomaj, CMIS 102 7383, 03/12/2022
print('This is my Python program for computing pay for a weekly paper carrier')

# set variables for cost newspaper, in this project we will use 10, Set variable for the amount the carrier recieves in this case we will use 30%
cost = 10
carriercut = float(0.30)

# these 3 lines represent the user prompted question, the values of each will be stored, and used in later computations, floats represent fractions and int represnts a whole number
route = int(input('how many papers did you deliver on the route?: '))
days = float(input('how many days did you deliver papers this week?: '))
tips = float(input('how much did you make in tips '))

#salary represents the user inputs listed above, multiplied by eacher other, we then print salary along with some strings to give the total weekly salary
salary = route * days * carriercut
print('your weekly salary is', salary, 'dollars')

#totalpay takes the salary variable from above and performs addition with the tips variable  to give total money earned that week, this is printed alongside strings
totalpay = salary + tips
print('your total pay for this week which includes your weekly salary + tips is', totalpay, 'dollars')