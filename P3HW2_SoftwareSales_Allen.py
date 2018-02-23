# CTI-110
# P3HW1 - Software Sales
# Allen, Joshua
# 2/22/2018
#
software_purchased = int(input("software purchased: " ))
software_purchased = int(software_purchased)
def main():
    print("purchased")


discount = 0
total = 0
software_price = 99 * software_purchased

if software_purchased >= 100:
    discount = software_price * .40
    
elif software_purchased >= 50:
    discount = software_price * .30
    
elif software_purchased >= 20:
    discount = software_price * .20
    
elif software_purchased >= 10:
    discount = software_price * .10
    
total = software_price - discount


print ("Software Price: $",software_price)
print ("Total discount: $",discount)
print ("Total Price: $",total)
