#Factorial
#Allen, Joshua
#CTI-110
#12MAR2018

number = int(input("Please enter a number: "))
factorial = 1
             
for number in range( 1, number + 1 ):
    factorial = factorial * number

print("The factorial of", number, "is", factorial)
