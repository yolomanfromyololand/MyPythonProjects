# Author: Yaroslav
# Date: 2026-11-12
# Purpose: Practice handling two different exceptions with two except clauses, printing Python’s error message with as, and using finally.
def read_first_number(filename):
    try:
        file = open(filename, "r")
        line = file.readline()
        file.close()

        value = int(line.strip())
        print("The first number in", filename, "is", value)

    except FileNotFoundError:
        print("Error: the file", filename, "was not found.")

    except ValueError as exception:
        print("Error:", str(exception))

    finally:
        print("Finished checking", filename)


def main():
    read_first_number("number.txt")
    read_first_number("missing.txt")
    read_first_number("badnumber.txt")


main()
