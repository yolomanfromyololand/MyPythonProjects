# Author: Yaroslav Davydenko        
# Date: 2026-09-30
# Purpose: Practice defining a function with multiple parameters, using a default parameter, and passing arguments using positional arguments..
def compute(num1, num2, operation='+'):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Division by zero"
        return num1 / num2
    else:
        return "Invalid operation"
 
 
def main():
    num1 = int(input("Enter number 1: "))
    operation = input("Operator (+, -, *, /): ")
    num2 = int(input("Enter number 2: "))
    result = compute(num1, num2, operation)
    print(f"Result: {result}")
 
 
print(compute(13, 45, '*'))
print(compute(13, 45, '/'))
print(compute(13, 45, '-'))
print(compute(13, 45, '+'))
print(compute(13, 45))  
 
main()


    
    
    