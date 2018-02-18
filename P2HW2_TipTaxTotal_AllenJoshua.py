# CTI-110
# P2HW2 - Tip Tax Total
# Joshua Allen
# 2/17/2018
# Calculating Tip and Tax at a Resturant
foodCost = float(input("Cost of Meal?"))
salestax = 0.07
tip = 0.18
print ("Taxes $", format(foodCost * 0.07, ',.2f'))
print ("Gratudity $", format(foodCost * 0.18, ',.2f'))
print ("Grand Total $", format((foodCost * salestax)+(foodCost * tip) + foodCost, ',.2f'))

