# Conditionals

x = 7


# basic if
if x < 6:
    print("This is true")


#if else
if x < 6:
    print("True")
else:
    print("this is false")


#elif (else-if)
color = 'red'

if color == 'red':
    print('color is red')
elif color == 'blue':
    print('color is blue')
else:
    print('color is not red or blue')


#nest if
    if color == 'red':
        if x < 10:
            print('color is red and less than ten')


#Logical operators
if color == 'red' and x < 10:
    print('color is red and less than ten')
