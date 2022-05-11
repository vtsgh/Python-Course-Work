# Vangjel Thomaj CMIS 102 7383 April 9th 2022
print('Hello, this is my program for assignment 5')


# list of names that will be passed thru the function
names = ['bob', 'katie', 'jack', 'alex']

# function that contains the prompts + weighted average + print statement + return for variable total
def weighted_average(student):

    disc = float(input('what is your discussion grade?: '))
    quiz = float(input('what is your quiz grade?: '))
    prog = float(input('what is your programming assignment grade?: '))
    discgrade = disc * .25
    quizgrade = quiz * .30
    prograde = prog * .45
    total = (discgrade + quizgrade + prograde)
    print('Hello', student, 'your weighted average is', total)
    return total

# variables for the loop to use
largest = None
winner = None

# for loop that iterates thru the list of names, calling total to equal weighted average.
# also the if statement that checks to see which student has the highest grade in the class and their name
for student in names:

    total = weighted_average(student)

    if largest is None or largest < total:
        largest = total
        winner = student

# print statement outside the function and loop, that prints the highest score + student,
# after the loop finishes.
print('Wow!!!!', winner, 'you have highest average so far at', largest)











