# Author: Yaroslav Davydenko
# Date: 2026-10-27
# Purpose: Combine Python statements and matching machine code into one file.


def merge_files(py_filename, code_filename, out_filename):
    a = open(py_filename, "r")
    b = open(code_filename, "r")
    c = open(out_filename, "w")
    line = a.readline()
    d = b.readline()
    while line != "" and d != "":
        line = line.split('#')[0].strip()
        d = d.strip()
        c.write(line + '\t' + d + '\n')
        line = a.readline()
        d = b.readline()
    a.close()
    b.close()
    c.close()


def main():
    merge_files("pythonStatements.txt", "machineCode.txt", "output.txt")
    print("output.txt has been created")


main()
