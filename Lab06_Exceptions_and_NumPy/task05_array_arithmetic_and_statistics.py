# Author: Yaroslav
# Date: 2026-11-12
# Purpose: Practice element-wise arithmetic, broadcasting, and NumPy’s statistical functions.
import numpy as np


def array_arithmetic(arr1, arr2):
    print("arr1:", arr1)
    print("arr2:", arr2)
    print("arr1 + arr2:", arr1 + arr2)
    print("arr1 - arr2:", arr1 - arr2)
    print("arr1 * arr2:", arr1 * arr2)
    print("arr1 ** 2:", arr1 ** 2)
    print("arr1 + 10:", arr1 + 10)
    print("arr2 * 2:", arr2 * 2)


def print_statistics(data):
    print("Total:", np.sum(data))
    print("Average:", round(np.mean(data), 2))
    print("Median:", np.median(data))
    print("Maximum:", np.max(data))
    print("Minimum:", np.min(data))


def main():
    print("=== Array arithmetic ===")
    arr1 = np.array([2, 4, 6, 8])
    arr2 = np.array([1, 3, 5, 7])
    array_arithmetic(arr1, arr2)

    print()
    print("=== Daily login attempts ===")
    logins = np.array([15, 22, 13, 40, 30, 27, 18])
    print_statistics(logins)


main()

# NumPy uses broadcasting to apply the scalar value 10 to every element of arr1.
# The addition is performed element by element by NumPy so no explicit Python loop is needed.
