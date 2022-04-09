# Vangjel Thomaj CMIS 102 7383 April 6th 2022
print('Hello, this is my program for Discussion 5')

#It is a program that loops between inputs for choices at a farmers market sale
#the program keeps cyling thru options until the spending limit of 100 or more dollars is reached
# n = 0 means the current amount that we have spent is 0 dollars
n = 0

#while loop stated that as long as the value of n is lower than 100, the program will continue to loop
#there are various options for the user to either spend money on, not spend money or even gain money
while n <= 100:

#user has to choose between blueberries and raspberries
    berries = input('Here we are at the start of the farmers market,'
                    'You notice some berries for sale, '
                    'what kind of berries would you like to buy, blueberries for $10, or raspberries for $15? '
                    'Type blueberries or raspberries: ')
    if berries == 'blueberries':
        n = n + 10
    elif berries == 'raspberries':
        n = n + 15

#user can choose between buying a bunch of bananas for 5 dollars or not
    banana = input('Next is bananas do you want to buy a bunch of bananas for 5 dollars? '
                   'if so type yes, if not type no: ')
    if banana == 'yes':
        n = n + 5
    elif banana == 'no':
        n = n

#user can choose between organic and normal appples for different price points per apple
#the user can then choose how many apples of the selected kind of apple they want to buy
    apple = input('Then we have apples,Organic cost 2 dollars per apple, and normal cost 1 dollar per apple.'
                  ' would you like to buy organic or normal apples: ')
    if apple == 'organic':
        organicapple = int(input('How many organic apples would you like to buy up to a maximum of 10?: '))
        n = n + (2 * int(organicapple))
    elif apple == 'normal':
        normalapple = int(input('How many normal apples would you like to buy?: '))
        n = n + (1 * int(normalapple))

#user can gain back 5 dollars to continue spending thus needing to spend more money to break the loop
#user can give back the money they found to remain on track
    money = str(input('Oh no! someone in front of you has dropped a $5 bill, are you going to return it, yes or no?: '))
    if money == 'yes':
        n = n
    elif money == 'no':
        n = n - 5

#user can choose between a tree at various price points
#asuming the user chose the most expensive options they will still not be able to break the loop
#they will be redirected back to the start to buy more things, the value of n continues to grow
    tree = str(input('At the end of the farmers market you notice 3 beautiful plants for sale, '
                     'but you only have room for one! Which will you buy? '
                     'The Bamboo Palm Tree, The japanese Cherry Blossom tree, or the Bonsai tree, '
                     'type BPT or JCBT or BT: '))

    if tree == 'BPT':
        n = n + 35
    elif tree == 'JCBT':
        n = n + 40
    elif tree == 'BT':
        n = n + 30

#print statement prints at the last option and loops the user back to berries options if user not yet spent 100 dollars or more
    if n <= 100:
        print('For some reason I do not feel like leaving the farmers market after only spending', n, 'dollars, back to the start we go!')

#print statement prints after the user escapes the loop by making n >=100, which would turn the while loop false, thus off
print('Ah Ha, We finally left the super market after spending', n, 'dollars, it felt like we were stuck in a loop!')