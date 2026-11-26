# Author: Yaroslav Davydenko
# Date: 2026-09-23
# Purpose: Use a while loop to repeatedly prompt the user until a valid PIN is entered.
pin = input("Please type in your PIN: ")

while pin != "1234":
    if len(pin) != 4 or not pin.isdigit():
        print("Incorrect. Enter a 4 digit number")
    else:
        print("Incorrect. try again")
    print()
    pin = input("Your PIN: ")

print("Correct PIN! ")