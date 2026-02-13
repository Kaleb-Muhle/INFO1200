#!/usr/bin/env python3
# display a welcome message
print("Welcome to Kaleb Muhlestein's Future Value Calculator")
#print: new line
print()
#set: control variable for loop
choice = "y"
#start: loop
while choice.lower() == "y":
    # get input from the user
    is_valid = False
    while not is_valid:
        monthly_investment = float(input("Enter monthly investment:\t"))
        if monthly_investment <= 0 and monthly_investment <=1000:
            print("Monthly investment must be greater than zero. Please try again.")
    yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
    years = int(input("Enter number of years:\t\t"))
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12
    # calculate the future value
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount
    # display the result
    print("Future value:\t\t\t" + str(round(future_value, 2)))
    print()
    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
print()
print("Bye!")
