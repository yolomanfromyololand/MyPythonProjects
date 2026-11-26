# Author: Yaroslav Davydenko
# Date: 2026-10-27
# Purpose: This program demonstrates how to write to a text file and read from it using different methods in Python.
def write_fruits(filename):
    f = open("filename", "w")
    f.write('1. Apples are crunchy.\n2. Oranges are sweet, sour and juicy.\n3. Strawberries are sweet.\n4. Which fruit do you like?')
    f.close()

def append_line(filename, text):
    f = open("filename", "a")
    f.write(text)
    f.close()
def print_file_lines(filename):
    f = open("filename", "r")
    line = f.readline()
    while line !="":
        print(line.strip())
        line = f.readline()
    f.close()

def main():
    write_fruits("fruits.txt")
    print("File fruits.txt has been created")

    append_line("fruits.txt", "\n5. Bananas are my favourite!")
    print("A new line has been appended to fruits.txt")

    print("Reading the file fruits.txt ...")
    print_file_lines("fruits.txt")
main()