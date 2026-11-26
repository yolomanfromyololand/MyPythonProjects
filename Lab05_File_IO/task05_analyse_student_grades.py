# Author: Yaroslav Davydenko
# Date: 2026-10-27
# Purpose: Load student grades into a dictionary and analyse them.


def load_grades(names_filename, grades_filename):
    a = open(names_filename, "r")
    b = open(grades_filename, "r")
    c = {}
    line = a.readline()
    d = b.readline()
    while line != "" and d != "":
        line = line.strip()
        d = int(d.strip())
        c[line] = d
        line = a.readline()
        d = b.readline()
    a.close()
    b.close()
    return c


def top_student(grades):
    a = ""
    b = -1
    for c in grades:
        if grades[c] > b:
            a = c
            b = grades[c]
    return a


def average_grade(grades):
    a = 0
    for b in grades:
        a = a + grades[b]
    return a / len(grades)


def main():
    grades = load_grades("students.txt", "grades.txt")
    print("Dictionary after reading files")
    print(grades)
    print()
    print("Analysis")
    a = top_student(grades)
    print(f"Highest grade: {a} with {grades[a]}")
    print(f"Average grade: {round(average_grade(grades), 1)}")


main()
