Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#Vangjel Thomaj, CMIS 102 7383, 03/10/2022

print('Hello class this is my week 2 Discussion post')
Hello class this is my week 2 Discussion post

# this line takes a users numerical input (float allows fraction representation) float makes it so that if anyone types a letter or character it gives back an error.

kg = float(input('please enter your weight in kg: '))
please enter your weight in kg: 68.0389

#this line also does what the previous line does, however instead of assigning using the variable kg to represent the inpput of weight, it uses m to represent the input of height

m = float(input('please enter your height in meters: '))
please enter your height in meters: 1.80259

#this line represents the equation used to calculate the users input, it works by assigning bmi to the remainder of the inputs of kg and m squared (** represents to the power of x, so in this case 1.80259 to the power of 2, or BMI=kg/m**2.)

bmi = kg / m**2

#this line allows us to print bmi, which will return the remainder of the given inputs

print('your body mass index is', bmi)
your body mass index is 20.93935832089704

