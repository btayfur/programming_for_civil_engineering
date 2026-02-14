# Calculate the area of a foundation footing
width = 2.5  # meters
length = 3.0 # meters

area = width * length

print("Footing Width:", width, "m")
print("Footing Length:", length, "m")
print("Footing Area:", area, "m^2")

# The difference between a calculator and a programming 
# script lies in here. Please notice we didnt use dimensions
# in the calculation. We used variables instead. In advance, 
# we can code this script like following:

#read inputs from user
width = float(input("Enter footing width (m): "))
length = float(input("Enter footing length (m): "))

#calculate area
area = width * length

#print results
print("Footing Width:", width, "m")
print("Footing Length:", length, "m")
print("Footing Area:", area, "m^2")