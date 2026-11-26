# Author: Yaroslav Davydenko        
# Date: 2026-09-30
# Purpose: Brief description of what the program does.
def has_even_number(numbers):
    for num in numbers:
        if num % 2 == 0:
            return True
    return False
            
my_list = [5, 3, 9, 7]

functionresult = has_even_number(my_list)
print(functionresult)