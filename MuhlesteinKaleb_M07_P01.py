#!/usr/bin/env python3
"""
Name: Kaleb Muhlestein
Class: INFO 1200
Section: 001
Professor: Professor AlSobeh
Date: 04/01/2026
Assignment: Module 7 Project
By submitting this assignment, I declare that the source code contained in this assignment was written 
solely by me, unless specifically provided in the assignment. I attest that no part of this assignment,
in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment
instructions, nor obtained from a subscription service. I understand that copying any source code,
in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that
I will receive a zero on this project if I am found in violation of this policy.
"""

#import tkinter from Python library for GUI
import tkinter as tk
#import math module for the square root function
import math

#define the function that we use to calculate
def theoremCalculator(entryA, entryB, resultLabel):
    #take entry from user for a side
    a = float(entryA.get())
    #take entry from user for b side
    b = float(entryB.get())
    #run the function from my other module
    c = pythagoreanTheorem(a, b)
    #modify the label to display the output, stored in the c variable
    resultLabel.config(text=f"c = {c}")

#define the function to clear all entries
def clearFields(entryA, entryB, resultLabel):
    #delete entries from the first field
    entryA.delete(0, tk.END)
    #delete entries from the second field
    entryB.delete(0, tk.END)
    #delete entries from the results field
    resultLabel.config(text="c = ")

#define the function to calculate the hypotenuse using the Pythagorean Theorem
def pythagoreanTheorem(a, b):
    #calculate the square of a and b, add them together, and take the square root to find c
    c = math.sqrt(a**2 + b**2)
    return c

#define main function to store the primary code
def main():
    #create the GUI named root
    root = tk.Tk()
    #title the GUI
    root.title("Pythagorean Theorem Solver")
    
    #create label to prompt user for side a
    tk.Label(root, text="Side a:").grid(row=0, column=0, padx=10, pady=5)
    #entry box for user to type into
    entryA = tk.Entry(root)
    #placement of entry
    entryA.grid(row=0, column=1, padx=10, pady=5)

    #create label to prompt user for side b
    tk.Label(root, text="Side b:").grid(row=1, column=0, padx=10, pady=5)
    #entry box for user to type into
    entryB = tk.Entry(root)
    #placement of second entry
    entryB.grid(row=1, column=1, padx=10, pady=5)

    #create area for results to be displayed
    resultLabel = tk.Label(root, text="c = ")
    #placemenmt of results displayed, beloy the entries
    resultLabel.grid(row=3, column=0, columnspan=2, pady=10)

    #create a button for users to calculate based on inputs, calling the previous function
    calcButton = tk.Button(root, text="Calculate", command=lambda: theoremCalculator(entryA, entryB, resultLabel))
    #place button below entries but above the display results
    calcButton.grid(row=2, column=0, columnspan=2, pady=10)

    #create a clear button to clear all fields, running the clearFields command
    clearButton = tk.Button(root, text="Clear", command=lambda: clearFields(entryA, entryB, resultLabel))
    #placement of the clear button, at the very bottom of the GUI
    clearButton.grid(row=4, column=0, columnspan=2, pady=10)

    #run the GUI
    root.mainloop()

#only run if main file    
if __name__ == "__main__":
    #run the main code
    main()