#Kaleb Muhlestein validation file for the Future Value App

def get_float(prompt, low, high):
    while True:
        number = float(input(prompt))
        if number > low and number<= high:
            return number
            break
        else:
            print("Entry must be greater than", low, "and less than or equal to", high)
            continue

def get_int(prompt, low, high):
    while True:
        number = int(input(prompt))
        if number > low and number<= high:
            return number
            break
        else:
            print("Entry must be greater than", low, "and less than or equal to", high)
            continue

def main():
    choice = "y"
    while choice.lower() == "y":
        valid_number = get_float("Enter number: ", 0, 1000)
        print("Valid number =", valid_number)
        print()
        valid_integer = get_int("Enter integer: ", 0, 1000)
        print("Valid integer =", valid_integer)
        print()
        choice = input("Repeat? (y/n): ")
    print("Bye!")

if __name__ == "__main__":
    main()