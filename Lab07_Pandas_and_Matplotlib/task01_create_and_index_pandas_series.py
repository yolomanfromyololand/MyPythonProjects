# Author: Yaroslav
# Date: 2026-11-16
# Purpose: Practice creating Series from a list, a NumPy array and a dictionary, and accessing values by position and by label.

import numpy as np
import pandas as pd


def create_series():
    numbers = pd.Series([5, 10, 15, 20], name="Numbers")    # done for you
    print("Numbers (from a list):")
    print(numbers)
    print()

    # 1. Create a Series named Evens from the NumPy array np.array([2, 4, 6, 8]),
    #    store it in the variable evens, and print it like Numbers above
    evens = pd.Series(np.array([2, 4, 6, 8]), name="Evens")
    print("Evens (from a NumPy array):")
    print(evens)
    print()

    # 2. Create a Series named Ages from the dictionary {"Alice": 25, "Bob": 30, "Charlie": 35},
    #    store it in the variable ages, and print it like Numbers above
    ages = pd.Series({"Alice": 25, "Bob": 30, "Charlie": 35}, name="Ages")
    print("Ages (from a dictionary):")
    print(ages)
    print()

    return numbers, evens, ages


def access_values(numbers, ages):
    print("=== Accessing values ===")
    print("First value of Numbers:", numbers.iloc[0])      # done for you
    # 3. Print the last value of Numbers (use .iloc[-1])
    print("Last value of Numbers:", numbers.iloc[-1])
    # 4. Print the age of Bob (use the label "Bob")
    print("Age of Bob:", ages["Bob"])
    # 5. Print Numbers multiplied by 2, as a list (use .tolist())
    print("Numbers doubled:", (numbers * 2).tolist())


def main():
    numbers, evens, ages = create_series()
    access_values(numbers, ages)


main()
