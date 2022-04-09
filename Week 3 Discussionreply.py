#Program to determine age difference of siblings

#Greet the user
print('Hello. \nLet\'s find out the age difference between you and your siblings.')

#Prompt for user's sibling's and own age
user_age = eval(input('How old are you? '))
sister_age = eval(input('How old is your sister? '))
brother_age = eval(input('How old is your brother? '))
cousin_age = eval(input('How old is your cousin? '))

#Compute and display age difference between user and sister
if user_age < sister_age:
    sis_age_diff = sister_age - user_age
    print('You are', sis_age_diff, 'year(s) younger that your sister.')
elif user_age > sister_age:
    sis_age_diff = user_age - sister_age
    print('You are', sis_age_diff, 'year(s) older than your sister.')
else:
    print('You are the same age as your sister.')
    
#Compute and display age difference between user and brother
if user_age < brother_age:
    bro_age_diff = brother_age - user_age
    print('You are', bro_age_diff, 'year(s) younger that your brother.')
elif user_age > brother_age:
    bro_age_diff = user_age - brother_age
    print('You are', bro_age_diff, 'year(s) older than your brother.')
else:
    print('You are the same age as your brother.')

#compute and display age difference between user and cousin
if user_age < cousin_age:
    cous_age_diff = cousin_age - user_age
    print('You are', cous_age_diff, 'year(s) younger than your cousin.')
elif user_age > cousin_age:
    cous_age_diff = user_age - cousin_age
    print('You are', cous_age_diff, 'year(s) older than your cousin.')

else:
    print('You are the same age as your cousin.')