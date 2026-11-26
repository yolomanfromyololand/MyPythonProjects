# Author: Yaroslav Davydenko        
# Date: 2026-09-30
# Purpose: Practice using keyword arguments when calling a function and understand how keyword arguments allow arguments to be passed in a different order

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
    result = compute(num1=num1, num2=num2, operation=operation)
    print(f"Result: {result}")
 
   
    print(compute(num1=13, num2=45, operation='*'))
    print(compute(operation='/', num2=45, num1=13))
    print(compute(num2=45, num1=13, operation='-'))
    print(compute(num1=13, num2=45, operation='+'))
    print(compute(num1=13, num2=45))  
 
 
main()