# Author: Yaroslav
# Date: 2026-11-16
# Purpose: Practice filtering rows with a condition, sorting, and adding a flag column.

import pandas as pd


def build_grades():
    data = {
        "Name": ["Amira", "David", "Sofia", "Liam", "Noah", "Maya"],
        "Course": ["Math", "Math", "Science", "History", "Science", "History"],
        "Grade": [85, 92, 78, 88, 95, 71],
    }
    return pd.DataFrame(data)


def analyse_grades(df):
    # 1. Print the students with a grade above 90 (use df[df["Grade"] > 90])
    print("Grades above 90:")
    print(df[df["Grade"] > 90])
    print()
    # 2. Print the DataFrame sorted by grade, highest first (use sort_values with ascending=False)
    print("Sorted by grade (highest first):")
    print(df.sort_values("Grade", ascending=False))
    print()
    # 3. Add a flag column named Honours that is True when Grade is 85 or more
    #    (use df["Honours"] = df["Grade"] >= 85), then print the whole DataFrame
    df["Honours"] = df["Grade"] >= 85
    print("With an Honours column:")
    print(df)


def main():
    df = build_grades()
    print("Student grades:")
    print(df)
    print()
    analyse_grades(df)


main()
