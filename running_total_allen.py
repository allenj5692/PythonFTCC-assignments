#Running Total
#Allen, Joshua
#CTI-110
#12MAR2018
grade_num = 0
total = 0
grades = input("Please enter grade percentage or enter to exit:")

while grades != "":
    grade_num +=1
    grade_value = float(grades)
    total += grade_value
    grades = input("Please enter grade percentage or enter to exit:")
    
average = total/grade_num
print("Credit for the number of graded assignments:" ,grade_num)
print("your total is:" ,total)
print("Your Percentage is" ,average)          
        
