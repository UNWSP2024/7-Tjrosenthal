# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

#Tanner Rosenthal
#2/3/2025
#Distance Between Points

import math

def distance(tuple1, tuple2):
    x1 = tuple1[0]
    y1 = tuple1[1]
    z1 = tuple1[2]
    x2 = tuple2[0]
    y2 = tuple2[1]
    z2 = tuple2[2]

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"The distance between {tuple1} and {tuple2} is {distance:.2f}")

tuple1 = tuple(map(int, input("Enter the coordinates of a point separated by commas as (x, y, z)").split(',')))
tuple2 = tuple(map(int, input("Enter the coordinates of a point separated by commas as (x, y, z)").split(',')))

if len(tuple1) != 3 or len(tuple2) != 3:
    print("Input Error. Enter Exactly 3 Values")

else:
    distance(tuple1, tuple2)




# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2) 
