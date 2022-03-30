# Vangjel Thomaj CMIS 102 7383 March 29th 2022
print('Hello, this is my program for Assignment 4')

#these comments below represent the cleaning services and and price points for small,medium and large number of rooms
#"vacuuming": [8, 16, 24]
#"mopping": [6, 12, 18]
#"dusting": [5, 10, 15]

#these comments below represents the cut off amounts for the number of rooms which represent small medium and large
#"small room = 0-3 rooms
#"medium room = 4-9 rooms
#"large room = 10+ rooms

#these 4 lines of code represent the inputs of the users,rooms stores the number of rooms that the user wants to be cleaned
#while choices represents the type of cleaning service request
#light_complete represents the choices of either a light clean or a complete clean of the rooms
#total_rooms represents the total amount of rooms in the house that the user has
#str means that only strings will be accepted as inputs, where are int means that only whole numbers will be accepted as inputs
total_rooms = int(input('How many rooms are in your house total '))
light_complete = str(input('Do you want a light clean or a complete clean of your rooms? '))
choices = str(input('what type of cleaning service would you like, vacuuming, dusting or mopping? '))
rooms = int(input('how many rooms are you looking to have cleaned today? '))


#these lines of code represent the conditional requirement for certain lines of code to print
#in this case the code states that in order to execute the print line the following must be true
#choices needs to be equal to vacuuming, mopping or dusting, and rooms needs to fall within a range, in this case 0-3, 4-9, or 10+
#if the conditions are true then the realavent print statement will print, if they are false the print is skipped
def function1(choices, rooms):
#vacuuming
    if choices == 'vacuuming' and rooms >= 0 and rooms <= 3:
        print('vacuuming for a small number of rooms costs $8')
    if choices == 'vacuuming' and rooms >= 4 and rooms <= 9:
        print('vacuuming for a medium number of rooms costs $16')
    if choices == 'vacuuming' and rooms >= 10:
        print('vacuuming for a large number of rooms costs $24')
#mopping
    if choices == 'mopping' and rooms >= 0 and rooms <= 3:
        print('mopping for a small number of rooms costs $6')
    if choices == 'mopping' and rooms >= 4 and rooms <= 9:
        print('mopping for a medium number of rooms costs $12')
    if choices == 'mopping' and rooms >= 10:
        print('mopping for a large number of rooms costs $18')
#dusting
    if choices == 'dusting' and rooms >= 0 and rooms <= 3:
        print('dusting for a small number of rooms costs $5')
    if choices == 'dusting' and rooms >= 4 and rooms <= 9:
        print('dusting for a medium number of rooms costs $10')
    if choices == 'dusting' and rooms >= 10:
        print('dusting for a large number of rooms costs $15')

#light clean
if light_complete == 'light' and total_rooms >=0 and total_rooms <= 3:
    print('out of a total of', total_rooms, 'rooms, you want', rooms, 'rooms')
    function1(choices, rooms)
if light_complete == 'light' and total_rooms >=4 and total_rooms <= 9:
    print('out of a total of', total_rooms, 'rooms, you want', rooms, 'rooms')
    function1(choices, rooms)
if light_complete == 'light' and total_rooms >= 10:
    print('our of a total of', total_rooms, 'rooms, you want', rooms, 'rooms')
    function1(choices, rooms)

#complete clean
if light_complete == 'complete' and total_rooms >=0 and total_rooms <= 3:
    print('out of a total of', total_rooms, 'rooms, you want a complete clean of', rooms, 'rooms')
    function1(choices, rooms)
if light_complete == 'complete' and total_rooms >=4 and total_rooms <= 9:
    print('out of a total of', total_rooms, 'rooms, you want a complete clean of', rooms, 'rooms')
    function1(choices, rooms)
if light_complete == 'complete' and total_rooms >= 10:
    print('out of a total of', total_rooms, 'rooms, you want a complete clean of', rooms, 'rooms')
    function1(choices, rooms)

