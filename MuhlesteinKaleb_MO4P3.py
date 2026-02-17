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
#print: My name and name of app with a blank line for readability
print("Kaleb Muhlestein's Change App")
print()

#set: control variable to "y" to start the loop
choice = "y"
#start loop: while control variable is "y" or "yes"
while choice.lower() == "y" or choice.lower() == "yes":
    #check user is entering valid number
    try:
        #get: number of cents from user
        cents = int(input("Enter number of cents (0-99):\n"))
        #check: number of cents is within the valid range of 0 to 99
        if cents < 0 or cents > 99:
            #display error message for user
            print("Please enter a number between 0 and 99.")
            #make user try again if they enter a number outside the valid range
            continue
    #direct: all non integer inputs here
    except ValueError:
        #print: error message directing user to try again
        print("Invalid input. Please enter a valid integer between 0 and 99.")
        #make user try again if they enter a non-integer for cents
        continue
    print ()
    #calculate: number of quarters, dimes, nickels and pennies by leaving the remainder for the following coin
    quarters = round(cents // 25)
    cents = cents % 25
    dimes = round(cents // 10)
    cents = cents % 10
    nickels =  round (cents // 5)
    cents = cents % 5
    pennies = cents
    print("Quarters:", quarters)
    print("Dimes:", dimes)
    print("Nickels:", nickels)
    print("Pennies:", pennies)
    print()
    #ask user if they want to continue, breaking loop on any input other than "y" or "yer"
    choice = input("Continue? (y/n):\n")
    print()

#print: goodbye message for user
print("Bye!")