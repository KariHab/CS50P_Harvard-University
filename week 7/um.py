import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    #returns, as an int, the number of times that “um” appears in that text, case-insensitively
    return len(re.findall(r"\b[uU]m\b", s))

if __name__ == "__main__":
    main()