import sys
import csv
import os.path
from os import path


if len(sys.argv) <3:
    sys.exit("too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("too many command-line arguments")
elif not path.exists(sys.argv[1]):
    sys.exit("file does not exist")
else:
    file_read = open(sys.argv[1], "r")
    reader = csv.reader(file_read, delimiter =",")
    headers = next(reader)
    column = ["first", "last", "house"]
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=column)
        writer.writeheader()
        for row in reader:
            name, house = row
            last, first = name.split(",")
            writer.writerow({"first": first.strip(" "), "last": last, "house": house})