# Author: Yaroslav
# Date: 2026-11-16
# Purpose: Practice building a DataFrame from a dictionary and looking at its columns, rows and size.

import pandas as pd


def build_books():
    data = {
        "Title": ["The Great Gatsby", "A Brief History of Time", "To Kill a Mockingbird",
                  "The Art of Computer Programming", "Sapiens"],
        "Author": ["F. Scott Fitzgerald", "Stephen Hawking", "Harper Lee",
                   "Donald Knuth", "Yuval Noah Harari"],
        "Year": [1925, 1988, 1960, 1968, 2011],
        "Pages": [180, 212, 281, 672, 498],
    }
    # 1. Convert data to a DataFrame with pd.DataFrame(), store it in books, and return books
    books = pd.DataFrame(data)
    return books


def explore_books(books):
    print("All books:")
    print(books)                 # done for you
    print()
    # 2. Print the Title column
    print("Title column:")
    print(books["Title"])
    print()
    # 3. Print the first 3 rows (use .head(3))
    print("First 3 rows:")
    print(books.head(3))
    print()
    # 4. Print the number of rows and columns (use .shape)
    print("Rows and columns:", books.shape)
    # 5. Print the author of the book in row 2 (use .loc[2, "Author"])
    print("Author of the book in row 2:", books.loc[2, "Author"])


def main():
    books = build_books()
    explore_books(books)


main()
