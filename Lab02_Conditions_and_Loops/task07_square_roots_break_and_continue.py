# Author: Yaroslav Davydenko
# Date: 2026-09-23
# Purpose: To practice using break and continue statements in Python loops to control flow based on user input.

import math

while True:
    number = float(input("Number: "))

    if number < 0:
        print("Invalid number.")
        print()
        continue
    elif number == 0:
        print("Exiting.")
        break
    else:
        print(math.sqrt(number))
        print()