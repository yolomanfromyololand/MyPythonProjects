#Author: Yaroslav Davydenko
# Date: 2026-10-27
# Purpose: This program demonstrates how to write to a text file and read from it using different methods in Python. It also counts the number of words in each line of the text file.

def create_rhyme(filename):
    with open(filename, "w") as dataFile:
        dataFile.write("I made myself a snowball\nAs perfect as could be.\nI thought I'd keep it as a pet\nAnd let it sleep with me.")


def count_words(filename):
    dataFile = open(filename, "r")
    line = dataFile.readline()
    while line != "":
        line = line.strip()
        line = line.strip('.')
        words = line.split()
        word_count = len(words)
        print(f"{line} --- {word_count} words")
        line = dataFile.readline()
    dataFile.close()


def main():
    create_rhyme("rhyme.txt")
    count_words("rhyme.txt")


main()
