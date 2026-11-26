# Author: Yaroslav
# Date: 2026-11-12
# Purpose: Practice accessing parts of a 2D array, totalling rows and columns with axis, and reshaping, including handling the error when a reshape is impossible.
import numpy as np


def explore_matrix(matrix):
    print("Failed logins (3 servers x 4 hours):")
    print(matrix)
    print(f"Shape: {matrix.shape} | Size: {matrix.size}")
    print("Server 2, hour 3:", matrix[1, 2])
    print("Server 1 (first row):", matrix[0])
    print("Hour 4 (last column):", matrix[:, -1])
    print("Servers 1-2, hours 1-2:")
    print(matrix[0:2, 0:2])
    print("Total per server:", np.sum(matrix, axis=1))
    print("Total per hour:", np.sum(matrix, axis=0))


def try_reshape(arr, shape):
    try:
        reshaped = arr.reshape(shape)
        print("Reshaped to", shape)
        print(reshaped)
    except ValueError as exception:
        print("Error:", str(exception))


def main():
    logins = np.array([15, 22, 13, 40, 30, 27, 18, 25, 11, 35, 20, 16])
    matrix = logins.reshape(3, 4)
    explore_matrix(matrix)

    print()
    print("=== Reshaping ===")
    try_reshape(logins, (4, 3))
    try_reshape(logins, (2, 2, 3))
    try_reshape(logins, (5, 3))


main()

# The original array contains 12 elements and reshaping must preserve the total number of elements.
# Shapes (4, 3) and (2, 2, 3) each require 12 elements while (5, 3) requires 15 so NumPy raises a ValueError.
