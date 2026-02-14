#!/usr/bin/env python3
# display a welcome message
print("Welcome to Kaleb Muhlestein's Future Value Calculator")
#print: new line
print()
#set: control variable for loop
choice = "y"
#start: loop that allows user to repeat calculator
while choice.lower() == "y":
    #set: control variable
    is_valid = False
    #start: loop that validates using control
    while not is_valid:
        #get: monthly investement from user
        monthly_investment = float(input("Enter monthly investment:\t"))
        #check to see if value is within logical range
        if monthly_investment > 0 and monthly_investment <=1000:
            #edit: control variable to allow loop to end after accepted input
            is_valid = True
        #direct invalid inputs here
        else:
            #print: error message explaining valid entries to user
            print("Entry must be greater than 0 and less than or equal to 1000. Please try again.")
    #reset: control variable
    is_valid = False
    #start: loop that validates using control
    while not is_valid:
        #get: yearly interest rate from user
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        #check to see if user input is valid
        if yearly_interest_rate > 0 and yearly_interest_rate <=15:
            #edit control variable to allow loop to end after accepted input
            is_valid = True
        #direct invalid inputs here
        else:
            #print: error message explaining valid entries to the user
            print("Entry must be greater than 0 and less than or equal to 15. Please try again.")
    #reset control variable
    is_valid = False
    #start: loop that validates using control
    while not is_valid:
        #get: years from user
        years = int(input("Enter number of years:\t\t"))
        #check to see if user input is valid
        if years > 0 and years <= 50:
            #edit control variable to allow loop to end after accepted input
            is_valid = True
        #direct invalid inputs here
        else:
            #print: error message explaining valid entries to the user
            print("Entry must be greater than 0 and less than or equal to 50. Please try again.")
    # convert yearly interest rate to monthly interest rate
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    # convert years into months
    months = years * 12
    # set future value to 0 to make it global before the loop
    future_value = 0
    #start for loop that will calculate for total months
    for i in range(months):
        #increase value by investment amount
        future_value += monthly_investment
        #calculate the amount of interest each month
        monthly_interest_amount = future_value * monthly_interest_rate
        #increase the future value by interest accrued
        future_value += monthly_interest_amount
    # display the result
    print("Future value:\t\t\t" + str(round(future_value, 2)))
    #print: new line
    print()
    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
#print: new line
print()
#print: exit message
print("Bye!")
