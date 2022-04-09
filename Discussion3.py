# Vangjel Thomaj CMIS 102 7383 March 15th 2022

# intro to our program that calculates total cost for fishing in the trophy fishing lake.
print('Today we are going to go fishing at a trophy lake, This lake contains over 1000 bass that weigh over 15 pounds! But, it can be a bit pricy')
print('Lets see if we can find out our total cost for the day')

# these variables represent our needed inputs to calculate total cost of the trip
boatfee = float(input('Hey I forgot, how much does it cost to rent a boat in dollars and cents? '))
costperhour = float(input('My memory is hazy, how much does it cost per hour to fish in the lake in dollars and cents? '))
hoursfished = float(input('How much time will we spend in the lake in hours? '))

# this equation represets the hourly cost of fishing on the lake multiplied by the hours spent on the lake plus the boat rental fee which gives us total cost
# this prints totalcost so its visible as well as the word dollars after the number
totalcost = (costperhour * hoursfished) + boatfee
print(totalcost,'dollars')

# this line of code adds a conditional print based on the values of totalcost, basically if the value of total cost is greater than or equal to 0
# and less than or equal to 150, then print the statement below.
if totalcost >= 0 and totalcost <= 150:
    print('wow! that is a super good deal :D')

# this line of code is an extension of the previous. If the previous condition is not met, but this one is, then the print statement below will be printed
# the condition for this is if the total cost is greater then or equal to 150.1 and also less then or equal to 300, it will print.
elif totalcost >= 150.1 and totalcost <= 300:
    print('hmmm, well everyone has to have a hobby :)')

# this line is an extension of both the previous lines, if both of the previous conditions are not met, this condition  will apply.
# the condition for this print statement to be applied is that the value of totalcost must be over 300.
else:
    print('awww, guess we cant go fishing at the trophy lake :(')






