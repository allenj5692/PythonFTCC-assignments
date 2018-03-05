#bug collector assignment
#Joshua Allen

# Intialize the accumulator.
total = 0

# Get the bugs collected for each day.
for day in range(1, 8):
    print("Enter the bugs collected on day", day)
    bugs = int(input())
    total += bugs

# Display the total bugs.
print ("You have collected a total", total, "bugs.")
