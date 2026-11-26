# Author: Yaroslav
# Date: 2026-11-12
# Purpose: Create NumPy arrays and inspect their attributes.

import numpy as np


def print_info(label, arr):
    print(label)
    print(arr)
    print(f"ndim: {arr.ndim} | shape: {arr.shape} | size: {arr.size} | dtype: {arr.dtype}")
    print()


def create_arrays():
    array1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    print_info("array1 (np.array):", array1)

    array2 = np.linspace(10, 100, 10)
    print_info("array2 (np.linspace):", array2)

    array3 = np.arange(10, 101, 10)
    print_info("array3 (np.arange):", array3)

    array4 = np.array([[1, 2, 3], [4, 5, 6]])
    print_info("array4 (2D):", array4)


def create_special_arrays():
    print_info("Zeros 2x4:", np.zeros((2, 4)))
    print_info("Ones 1D:", np.ones(5))
    print_info("Diagonal:", np.diag([4, 6, 1, 3]))
    print_info("Identity 3x3:", np.eye(3))


def main():
    print("=== Creating arrays ===")
    create_arrays()
    print("=== Special arrays ===")
    create_special_arrays()


main()
