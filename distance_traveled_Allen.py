#Joshua Allen
#CTI-110-0902
#Distance Traveled P4HW1
#12MAR2018

vehicleSpeed = int(input("What is the speed of the vehicle in mph?: "))
timeTraveled = int(input("How many hours has it traveled?: "))
print("Hour","\tDistance Traveled")
for currentHour in range( 1, timeTraveled + 1 ):
    distanceTraveled = vehicleSpeed * currentHour
    print(currentHour,"\t",distanceTraveled)
