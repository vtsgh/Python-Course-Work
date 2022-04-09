# Vangjel Thomaj CMIS 102 7383 March 27th 2022
#program calculates the Surface Area of a rectangle, it is wrapped within a function as intended for the discussion
print('Hello this is my discussion post for week 4,')
print('I see you want to know the surface area of your rectangle box, first ill need some information')

#variables and their demanded inputs, we cast string for name, and floats for the rest
name = str(input('First what is your name? '))
length = float(input('Second what is the length of the rectangle in ft? '))
width = float(input('Third what is the width of the rectangle in ft? '))
height = float(input('Fourth what is the height of the rectangle in ft? '))

#function takes 4 arguments, name and the dimension variable
#SA equation is 2LW + 2LH + 2HW, the variables values are given as inputs by the user
#the function then prints the surface area of the box and the users name + strings
def rectanglecalc(name, length, width, height):
    Surface_Area = (2 * length * width) + (2 * length * height) + (2 * height * width)
    return print('Well', name, 'the surface area of your rectangle box is', Surface_Area, 'ft squared')


#this calls the function, then gives it the arguments, in this case this variables we prompted for earlier
rectanglecalc(name, length, width, height)

