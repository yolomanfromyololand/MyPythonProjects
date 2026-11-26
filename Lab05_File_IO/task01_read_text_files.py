# Author: Yaroslav Davydenko
# Date: 2026-10-27
# Purpose: This program demonstrates how to read a text file using different methods in Python.
def read_whole_file(filename):
    f = open("data2.txt", "r")
    readfile1 = f.read()
    f.close()
    print(readfile1)

    pass


def read_first_two_lines(filename):
    f = open("data2.txt", "r")
    line1 = f.readline()
    line2 = f.readline()
    f.close()
    print(line1.strip())
    print(line2.strip())

    pass


def read_into_list(filename):
   
    with open("data2.txt", "r") as f:
        lines = f.readlines()
    print(lines)
    print(len(lines))
    print(lines[-1].strip())
    pass


def main():
    print("=== read() ===")
    read_whole_file("data2.txt")
    print("=== readline() ===")
    read_first_two_lines("data2.txt")
    print("=== readlines() ===")
    read_into_list("data2.txt")


main()