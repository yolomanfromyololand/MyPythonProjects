# Author: Yaroslav Davydenko        
# Date: 2026-09-30
# Purpose: how to use *args to accept a variable number of arguments in a Python function. This allows the function to handle flexible input sizes.
def get_initials(*args):
    initials = []
    for name in args:
        initials.append(name[0])  
    return initials
 
 
result = get_initials("Samuel", "Ravi", "Chen", "Fatima")
print(result)
 

print(get_initials("Emma", "Maija", "Sophia"))
print(get_initials("John"))
print(get_initials("Olivia", "Ravi", "Chen", "Fatima"))
 