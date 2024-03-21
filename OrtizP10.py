# OrtizP10
# Programmer: Christiana Ortiz
# Email: cortiz116@cnm.edu
# Purpose: demonstrate how to define a class
# Python version 3.12

# import class
from Class_GeoPoint import GeoPoint

print('\nComparative Distance Calculator'
      '\nThis program will tell you which Southwestern US city is closest to the coordinates you provide.\n')

# main

# Read text file of coordinates
with open('Points.txt', 'r') as f:  # assumes file is in same directory
    locations = f.readlines()  # put the lines to a variable (list).

# initialize list
pointList = []

# process list
for line in locations:
    # split lat, lon, and description from each line
    lat, lon, description = line.strip().split(',')
    # Create GeoPoint for each set of coordinates
    newPoint = GeoPoint(float(lat), float(lon), description)
    pointList.append(newPoint)

# Begin loop
while True:

    # Ask user for location
    user_location = input("Enter your location coordinates in decimal degrees (lat, lon): ")
    lat, lon = [float(x) for x in user_location.split(',')]

    # Create point from user's location
    user_point = GeoPoint(lat, lon, 'User Location')

    # Iterate through point list and find the closest point
    closest = None
    min_distance = float('inf')
    for point in pointList:
        distance = user_point.Distance(point.Point)
        if distance < min_distance:
            min_distance = distance
            closest = point

    # Tell user which point is closest
    print(f"You are closest to {closest.Description} which is located at {closest.Point}")

    # Ask user if they would like to do another calculation - loop if 'y'
    do_another = input("\nWould you like to do another calculation (y/n)?: ")
    if do_another != "y":
        break

# goodbye message
print('\nThank you for using this program. Goodbye.')
