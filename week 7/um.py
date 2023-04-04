import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    #returns, as an int, the number of times that “um” appears in that text, case-insensitively
    #only um not in a word like yummy - \b matches the empty string, but only at the beginning or end of a word
    return len(re.findall(r"\b[uU]m\b", s))




if __name__ == "__main__":
    main()