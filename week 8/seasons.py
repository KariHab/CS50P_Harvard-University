from datetime import date
import sys
import inflect
import re

p = inflect.engine()

def main():
    print(get_birthday(input("Date of birth: ")))


def get_birthday(s):
    if matches := re.search(r"^([1-2]\d{3})-(0\d|1[0-2])-(0\d|1\d|2\d|30?1?)$", s):
        age = date.today() - date(int(matches.group(1)), int(matches.group(2)), int(matches.group(3)))
        return f'{p.number_to_words(age.days * 24 * 60, andword= "").capitalize()} minutes'

    else:
        sys.exit("invalid date")

if __name__ == "__main__":
    main()