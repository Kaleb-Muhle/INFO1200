#!/usr/bin/env python3

# display a welcome message
print("Kaleb Muhlestein's Miles Per Gallon application")
#print: new line
print()

#create: control variable for loop, allowing user to decide when to stop
another_trip = "y"
#Being loop
while another_trip.lower() == "y" or another_trip.lower() == "yes":
    #get: miles driven from user
    miles_driven = float(input("Enter miles driven: "))
    #get: gallons of gas used from user
    gallons_used = float(input("Enter gallons of gas used: "))
    #get: cost per gallon from user
    cost_per_gallon = float(input("Enter cost per gallon: "))
    #check for valid input for miles driven
    if miles_driven <= 0:
        #if invalid, display error message
        print("Miles driven must be greater than zero. Please try again.")
        #restart loop
        continue
    #check for valid input for cost per gallon
    elif cost_per_gallon <= 0:
        #if invalid, display error message
        print("Cost per gallon must be greater than zero. Please try again.")
        #restart loop
        continue
    #check for valid input for gallons used
    elif gallons_used <= 0:
        #if invalid, display error message
        print("Gallons used must be greater than zero. Please try again.")
        #restart loop
        continue
    #run when all inputs are valid
    else:
        #calculate: total gas cost
        total_gas_cost = round((gallons_used * cost_per_gallon), 1)
        #print: total gas cost so user can see it
        print("Total Gas Cost: ", total_gas_cost)
        #calculate: cost per mile
        cost_per_mile = round((total_gas_cost / miles_driven), 1)
        #print: cost per mile so user can see it
        print("Cost Per Mile: ", cost_per_mile)
        #calculate: miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        #print: miles per gallon so user can see it
        print("Miles Per Gallon: ", mpg)
    #prompt user to decide if they want to enter another trip
    another_trip = input("Get entries for another trip? (y/n): ")

#print: new line
print()
#print: goodbye message
print("Bye")