# Feet to Inches Converter
# 4/16/2018
# CTI-110 P5T2_FeetToInches
# Joshua Allen


#Constants Used
#Constant for the number of inches per foot
INCHES_PER_FOOT = 12

def main():
    feet = int(input('Enter number of feet: '))

    # Convert feet to inches
    print(feet, 'equals', feet_to_inches (feet), 'inches.')

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

main()
