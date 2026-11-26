AnnualIncome = int(input("Your income: "))
MartialStuatus = input("Are you single or married?: ")
tax = 0


if MartialStuatus == "single":
    if AnnualIncome <= 8000:
        tax = 800 + AnnualIncome * 0.10 
    elif AnnualIncome <= 32000:
        tax = 800 + (AnnualIncome - 8000) * 0.15 
    else:
        tax = 4400 + (AnnualIncome - 32000) * 0.25
elif MartialStuatus == "married":
    if AnnualIncome <= 16000:
        tax = AnnualIncome * 0.10 
    elif AnnualIncome <= 64000:
        tax = 1600 + (AnnualIncome - 16000) * 0.15 
    else:
        tax = 8800 + (AnnualIncome - 64000) * 0.25

print(f"Your tax is: {tax}") 




