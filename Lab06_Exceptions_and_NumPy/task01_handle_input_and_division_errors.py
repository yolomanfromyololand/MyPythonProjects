# Author: Yaroslav
# Date: 2026-11-12
# Purpose:  Practice catching a ValueError and a ZeroDivisionError, and asking the user to correct their input instead of letting the program crash.
def get_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("That is not a whole number. Please try again.")
  


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: you cannot divide by zero.")
        return None

    


def main():
    numerator = get_integer("Enter the numerator: ")
    denominator = get_integer("Enter the denominator: ")
    result = divide(numerator, denominator)
    if result is not None:
        print(numerator, "/", denominator, "=", result)
    print("Program finished normally.")


main()
