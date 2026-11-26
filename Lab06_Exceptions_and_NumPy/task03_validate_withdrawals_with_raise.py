# Author: Yaroslav
# Date: 2026-11-12
# Purpose: Practice detecting an error with raise inside a function, and handling it with try/except in the caller.
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")
    if amount > balance:
        raise ValueError("Amount exceeds balance")
    return balance - amount


def main():
    balance = 500
    withdrawals = [100, 600, -50, 250]
    print("Starting balance:", balance)

    for amount in withdrawals:
        try:
            balance = withdraw(balance, amount)
            print("Withdrew", amount, "- new balance:", balance)
        except ValueError as exception:
            print("Withdrawal of", amount, "failed:", str(exception))

    print("Final balance:", balance)


main()
