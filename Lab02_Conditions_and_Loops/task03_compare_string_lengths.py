# Author: Yaroslav Davydenko
# Date: 2026-09-23
# Purpose: We use If-elif-else statement to print which string is longer
str1 = input("enter string 1: ")
str2 = input("enter string 2: ")
if len(str1) > len(str2):
    print("str1 is longer than str2!")
elif len(str2) > len(str1):
    print(f"{str2} is longer than {str1}!" )
else:
    print("string 1 and string 2 are of equal length!")
          