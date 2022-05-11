# while loop
while True:
    service = str(input('do you want house cleaning or lawn service?: '))

    if service == 'house cleaning' or service == 'House Cleaning':
        break

    if service == 'lawn service' or service == 'Lawn Service':
        break

if service == 'house cleaning' or service == 'House Cleaning':

    total_rooms = int(input('How many rooms are in your house total '))
    light_complete = str(input('Do you want a light clean or a complete clean of your rooms? '))
    choices = str(input('what type of cleaning service would you like, vacuuming, dusting or mopping? '))
    rooms = int(input('how many rooms are you looking to have cleaned today? '))
    discount = int(input('Seniors get a discount how old are you?: '))


    def service_and_cost(choices, rooms, discount):
    #vacuuming
        if choices == 'vacuuming' and rooms >= 0 and rooms <= 3 and discount < 60:
            print('vacuuming for a small number of rooms costs $20')
        elif choices == 'vacuuming' and rooms >= 4 and rooms <= 9 and discount < 60:
            print('vacuuming for a medium number of rooms costs $30')
        elif choices == 'vacuuming' and rooms >= 10 and discount < 60:
            print('vacuuming for a large number of rooms costs $40')
        elif choices == 'vacuuming' and rooms >= 0 and rooms <= 3 and discount >= 60:
            print('vacuuming for a small number of rooms with a senior discount costs $15')
        elif choices == 'vacuuming' and rooms >= 4 and rooms <= 9 and discount >= 60:
            print('vacuuming for a medium number of rooms with a senior discount costs $25')
        elif choices == 'vacuuming' and rooms >= 10 and discount >= 60:
            print('vacuuming for a large number of rooms with a senior discount costs $35')
    #mopping
        if choices == 'mopping' and rooms >= 0 and rooms <= 3 and discount < 60:
            print('mopping for a small number of rooms costs $50')
        elif choices == 'mopping' and rooms >= 4 and rooms <= 9 and discount < 60:
            print('mopping for a medium number of rooms costs $60')
        elif choices == 'mopping' and rooms >= 10 and discount < 60:
            print('mopping for a large number of rooms costs $70')
        elif choices == 'mopping' and rooms >= 0 and rooms <= 3 and discount >= 60:
            print('mopping for a small number of rooms with a senior discount costs $45')
        elif choices == 'mopping' and rooms >= 4 and rooms <= 9 and discount >= 60:
            print('mopping for a medium number of rooms with a senior discount costs $55')
        elif choices == 'mopping' and rooms >= 10 and discount >= 60:
            print('mopping for a large number of rooms with a senior discount costs $65')
    #dusting
        if choices == 'dusting' and rooms >= 0 and rooms <= 3 and discount < 60:
            print('dusting for a small number of rooms costs $80')
        elif choices == 'dusting' and rooms >= 4 and rooms <= 9 and discount < 60:
            print('dusting for a medium number of rooms costs $90')
        elif choices == 'dusting' and rooms >= 10 and discount < 60:
            print('dusting for a large number of rooms costs $100')
        elif choices == 'dusting' and rooms >= 0 and rooms <= 3 and discount >= 60:
            print('dusting for a small number of rooms with a senior discount costs $75')
        elif choices == 'dusting' and rooms >= 4 and rooms <= 9 and discount >= 60:
            print('dusting for a medium number of rooms with a senior discount costs $85')
        elif choices == 'dusting' and rooms >= 10 and discount >= 60:
            print('dusting for a large number of rooms costs $95')

    # light clean
    if light_complete == 'light' and total_rooms >= 0 and total_rooms <= 3:
        print('out of a total of', total_rooms, 'rooms, you want', rooms, 'rooms')
        service_and_cost(choices, rooms, discount)
    if light_complete == 'light' and total_rooms >= 4 and total_rooms <= 9:
        print('out of a total of', total_rooms, 'rooms, you want', rooms, 'rooms')
        service_and_cost(choices, rooms, discount)
    if light_complete == 'light' and total_rooms >= 10:
        print('our of a total of', total_rooms, 'rooms, you want', rooms, 'rooms')
        service_and_cost(choices, rooms, discount)

    # complete clean
    if light_complete == 'complete' and total_rooms >= 0 and total_rooms <= 3:
        print('out of a total of', total_rooms, 'rooms, you want a complete clean of', rooms, 'rooms')
        service_and_cost(choices, rooms, discount)
    if light_complete == 'complete' and total_rooms >= 4 and total_rooms <= 9:
        print('out of a total of', total_rooms, 'rooms, you want a complete clean of', rooms, 'rooms')
        service_and_cost(choices, rooms, discount)
    if light_complete == 'complete' and total_rooms >= 10:
        print('out of a total of', total_rooms, 'rooms, you want a complete clean of', rooms, 'rooms')
        service_and_cost(choices, rooms, discount)

# lawn service
if service == 'lawn service' or service == 'Lawn Service':

    choices1 = str(input('what type of cleaning service would you like, mowing, edging, or shrub pruning?: '))
    discount1 = int(input('Seniors get a discount how old are you?: '))

    if choices1 == 'mowing' and discount1 < 60:
        sqftyard = float(input('what is the size of your yard in square feet?: '))
        totalmowing = sqftyard * .020
        print('your total cost for mowing is', totalmowing)

    elif choices1 == 'edging' and discount1 < 60:
        lnftyard = float(input('what is the linear footage of the yards edges?: '))
        totaledging = lnftyard * 15
        print('your total cost for edging is', totaledging)

    elif choices1 == 'shrub pruning' and discount1 < 60:
        noshrubs = int(input('how many shrubs need pruning?: '))
        totalshrubs = noshrubs * 50
        print('your total cost for shrub pruning is', totalshrubs)

    elif choices1 =='mowing' and discount1 >= 60:
        sqftyard = float(input('what is the size of your yard in square feet?: '))
        totalmowing = (sqftyard * .020) - 5
        print('your total cost for mowing after senior discount is', totalmowing)

    elif choices1 == 'edging' and discount1 >= 60:
        lnftyard = float(input('what is the linear footage of the yards edges?: '))
        totaledging = (lnftyard * 15) - 5
        print('your total cost for edging with a senior discount is', totaledging)

    elif choices1 == 'shrub pruning' and discount1 >= 60:
        noshrubs = int(input('how many shrubs need pruning?: '))
        totalshrubs = (noshrubs * 50) - 5
        print('your total cost for shrub pruning with a senior discount is', totalshrubs)




