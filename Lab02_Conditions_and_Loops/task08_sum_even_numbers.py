# Author: Yaroslav Davydenko
# Date: 2026-09-23
# Purpose:To use a for loop and conditional logic to calculate the sum of all even numbers from 1 to 100.
total = 0
 
for number in range(1, 101):
    if number % 2 == 0:
        total += number
 
print(f"The sum of all even numbers from 1 to 100 is: {total}")