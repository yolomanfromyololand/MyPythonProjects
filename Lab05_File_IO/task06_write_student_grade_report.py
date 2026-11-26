# Author: Yaroslav Davydenko
# Date: 2026-10-27
# Purpose: Write, append, and display a student grade report.


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


def print_file_lines(filename):
    a = open(filename, "r")
    line = a.readline()
    while line != "":
        print(line.strip())
        line = a.readline()
    a.close()


def letter_grade(a):
    if a >= 90:
        return "A"
    elif a >= 80:
        return "B"
    elif a >= 70:
        return "C"
    else:
        return "D"


def write_report(grades, filename):
    a = open(filename, "w")
    a.write("Name\tGrade\tLetter\n")
    for b in grades:
        a.write(b + '\t' + str(grades[b]) + '\t' + letter_grade(grades[b]) + '\n')
    a.close()


def append_summary(grades, filename):
    a = open(filename, "a")
    a.write("Top student: " + top_student(grades) + '\n')
    a.write("Class average: " + str(round(average_grade(grades), 1)) + '\n')
    a.close()


def main():
    grades = load_grades("students.txt", "grades.txt")
    write_report(grades, "report.txt")
    append_summary(grades, "report.txt")
    print("report.txt has been created")
    print_file_lines("report.txt")


main()
