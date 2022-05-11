# Vangjel Thomaj CMIS 102 7383 April 21st 2022

# Function to check if the length of the password is within
# the range of 7-17 characters
# If it is not it returns true
def length_function():
    if not(len(password) >= 7 and len(password) <= 17):
        print('Your password does not meet the proper length')
    else:
        return True

# Function to check if there is at least one number in the password
# If there is not it returns true
def digit_function():

    digitcheck = any(chr.isdigit() for chr in password)

    if digitcheck == False:
        print('Your password needs to have a number in your name')
    else:
        return True

# Function to check if there is at least one letter in the password
# if there is not it returns true
def alpha_function():
    lettercheck = any(chr.isalpha() for chr in password)

    if lettercheck == False:
        print('Your password needs to have a letter in your name')
    else:
        return True

# Function to check if there is a space in the password
# if there is a space it returns false
def prohib_function():
    if password.find(' ') > 0:
        print('No spaces allowed')
    else:
        return False

# prompts the user to enter their password
password = input('Please enter your password: ')

# this is statement only executes the print statement that the password is valid if
# all conditions are met, the conditions are the opposite
# of the conditions that print that the password is incorrect
if length_function() == True and digit_function() == True and alpha_function() == True and prohib_function() == False:
    print('Your password is valid')


