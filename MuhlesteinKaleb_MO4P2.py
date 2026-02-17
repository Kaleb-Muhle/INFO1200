"""
Name: Kaleb Muhlestein
Class: INFO 1200
Section: 001
Professor: Professor AlSobeh
Date: 02/18/2026
Assignment: #3
By submitting this assignment, I declare that the source code contained in this assignment was written 
solely by me, unless specifically provided in the assignment. I attest that no part of this assignment,
in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment
instructions, nor obtained from a subscription service. I understand that copying any source code,
in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that
I will receive a zero on this project if I am found in violation of this policy.
"""
#print: assignement with my name and a blank line
print("Kaleb Muhlestein's Tip Calculator")
print()

#get: meal cost from user, repeating prompt until user enters a valid number
while True:
    try:
        #only accept floats for meal cost from user
        meal_cost = float(input("Cost of meal:\n"))
        #exit loop if user enters a valid number
        break
    #catch: value error and prompt user again if they enter a non-number for meal cost
    except ValueError:
        print("Invalid input. Please enter a number.")
#print: meal cost entered by user, sandwiched between blank lines for readability
print()
print("You entered:", meal_cost)
print()

#start: loop to calculate tip amounts for 15, 20 and 25 percent
for tip in(15, 20, 25):
    #print: tip percentage for user to see
    print("For a " + str(tip) + "% tip:")
    tip_percent = tip / 100
    tip_amount = round(meal_cost * tip_percent, 2)
    total = round(meal_cost + tip_amount, 2)
    #print tip amount for user to see
    print("Tip amount:", tip_amount)
    #print total amount for user to see
    print("Total amount:", total)