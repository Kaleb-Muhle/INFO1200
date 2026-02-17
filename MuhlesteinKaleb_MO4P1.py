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
#print: name of the assignemnt and a blank line
print("Kaleb Muhlestein's Letter Grade Converter")
print()

#set: control variable to "y" to start the loop
choice = "y"
#start loop: while control variable is "y" or "yes"
while choice.lower() == "y" or choice.lower() == "yes":
    #try: prompt user for numerical grade and reject integers
    try:
        #get: numerical grade from user
        number = int(input("Enter numerical grade:\n"))
        #determine: letter grade based on numerical grade, testing from a down to e
        if number >= 94 and number <= 100:
            letter = "A"
        elif number >= 90 and number <= 93:
            letter = "A-"
        elif number >= 87 and number <= 89:
            letter = "B+"
        elif number >= 84 and number <= 86:
            letter = "B"
        elif number >= 80 and number <= 83:
            letter = "B-"
        elif number >= 77 and number <= 79:
            letter = "C+"
        elif number >= 74 and number <= 76:
            letter = "C"
        elif number >= 70 and number <= 73:
            letter = "C-"
        elif number >= 67 and number <= 69:
            letter = "D+"
        elif number >= 64 and number <= 66:
            letter = "D"
        elif number >= 60 and number <= 63:
            letter = "D-"
        elif number >= 0 and number <= 59:
            letter = "E"
        #direct: numbers that are impossible for letter grades to an error message and prompt user again
        else:
            print("Invalid input. Please enter a  number between 0 and 100.")
            continue
        #display: letter grade to user
        print("Letter grade:", letter)
    #catch: value error if user enters a non-integer and prompt user again
    except ValueError:
        print("Invalid input. Please enter an integer between 0 and 100.")
        continue
    #determine: if user wants to continue or not, restarting loop on "y" or "yes"
    choice = input("Continue? (y/n)\n")

#print: goodbye message to user
print()
print("Bye!")