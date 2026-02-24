#!/usr/bin/env python3

def greet(name):
    print("Hello, " + name + "! Welcome to UVU.")

def calc_area(length, width):
    return length * width

def main():
    name = input("What is your name?\n")
    greet(name)
    while True:
        try:
            length = float(input("Enter the length of a parallelogram:\n"))
            break
        except ValueError:
            print("invalid input. Please enter a number.")
    while True:
        try:
            width = float(input("Enter the width of a parallelogram:\n"))
            break
        except ValueError:
            print("invalid input. Please enter a number.")
    area = calc_area(length, width)
    print("The area of the parallelogram is: " + str(round(area)))

if __name__ == "__main__":
    main()