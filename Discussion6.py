# introduction to my program for Discussion 6
# using """ to space and new line my strings
intro1 = """
                                                                        Vangjel Thomaj
                                                                        CMIS 102 7383
                                                                        April 14th 2022
                                                                        Discussion 6
"""
# using .center method specifically for the * padding
# not to actually center intro1
cent = intro1.center(800, "*")
print(cent)

# the start of the program where ther user is prompted for an input
print("""
You stand accused of taking cookies from the cookie jar.
A crime punishable to the fullest extent of the law.
The problem is.... You do not remember if you took the cookies or not!
Your lawyer has informed you that the best way to proceed, is to plead innocent.
The judge will now ask you for your alibi.
Please provide an alibi below.
""")
answer1 = str(input('greetings your honor, '))

# this for loop is where the initials v and t are counted to see how many time
# my initials pop up during the string
letter_v = 0
letter_t = 0
for letter in answer1:
    if letter == 'v' or letter == 'V':
        letter_v = letter_v + 1

    if letter == 't' or letter == 'T':
        letter_t = letter_t + 1

# this is where the number of times my initials are printed show up
print('\nIt would appear that the initial of your first name v shows up lower case or uppercase in your alibi a total amount of ' + str(letter_v) + ', the judge finds this awfully suspicious...')
print('It would also appear that the initial of your last name t shows up lowercase or uppercase in your alibi a total amount of ' + str(letter_t) + ', the judge finds this awfully suspicious...')

# this where the user is prompted for a 2nd input string
print('''
It appears the cookies were taken around 6:30 pm. The judge asks you to explain
exactly where you were, why you were there, what you were doing, and for how long.
''')
answer2 = str(input('Well... you see your honor, '))

# this is where the string is converted to all upper case
print('\nyou notice the judge making weird faces, he turns to you and says, \'I am sorry I did not hear you, can you please repeat it\'')
print('\nExcuse me your honor, I said....', answer2.upper(), '!!!!!!!!')
print('\nIt would seem the judge still can not comprehend what you are saying, you theorize that saying everything backwards may help.')

# this reverses the 2nd input that the user was prompted for and prints it
x = answer2
stringlength = len(x)
slicedstring = x[stringlength::-1]
print('\n' + slicedstring)

# more print strings
print('\nThe judge still does not understand your side of the story but is charmed at your attempts to defend yourself and finds you innocent')
print('\nCongratulations!!!')