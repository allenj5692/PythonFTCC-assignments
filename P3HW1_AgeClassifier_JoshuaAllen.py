# CTI-110
# P3HW1 - Age Classifier
# Joshua Allen 
# 2/22/2018

userAge = int(input('Enter in Age:'))
if userAge <= 1:
    print('You are an infant')
elif userAge < 13:
    print('You are a child')
elif userAge < 20:
    print('You are a teenager')
elif userAge >= 20:
    print('You are an adult')
