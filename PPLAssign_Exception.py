#Name: Shalaka Pawar
#Mis: 111903095
# Division: 2 

# Program to raise an exception and handle it
# This program can be used to take integer input only

import sys

List1 = [ 'a', 0, 2 ]
for i in List1:
    try:
        print("Entered value = ", i)
        reciprocal = 1/int(i)
    except:
        print("Error found - ", sys.exc_info()[0])
        print("\nNext entry")
print("Reciprocal of number = ", reciprocal)

try:
    integer = int(input("Enter a number : ")) # If user enters a non-integer value then this line will give ValueError
except:
    print("Please enter an integer number only")
