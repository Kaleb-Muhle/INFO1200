#!/usr/bin/env python3
"""
Name: Kaleb Muhlestein
Class: INFO 1200
Section: 001
Professor: Professor AlSobeh
Date: 03/06/2026
Assignment: Module 5 Project
By submitting this assignment, I declare that the source code contained in this assignment was written 
solely by me, unless specifically provided in the assignment. I attest that no part of this assignment,
in whole or in part, was directly created by Generative AI, unless explicitly stated in the assignment
instructions, nor obtained from a subscription service. I understand that copying any source code,
in whole or in part, unless specifically provided in the assignment, constitutes cheating, and that
I will receive a zero on this project if I am found in violation of this policy.
"""

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def main():
    print("Kaleb's even or odd checker.")
    print()
    my_num = int(input("Enter an integer: "))
    if is_even(my_num):
        print("This is an even number.")
    else:
        print("This is an odd number.")

if __name__ == "__main__":
    main()