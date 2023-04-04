




import sys
import csv
import os.path
from os import path

# 2 command-line arguments - check the len and sys. exit if needed
if len(sys.argv) <3:
    sys.exit("too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("too many command-line arguments")

#sys exit if does not provide exactly two command-line arguments,or if the first cannot be read
elif not path.exists(sys.argv[1]):
    sys.exit("file does not exist")

#name of a csv file to read as input, whose columns are assumed to be, in order, name and house
else:
    file_read = open(sys.argv[1], "r")
    reader = csv.reader(file_read, delimiter =",")
#do not forget about the header to not count
    headers = next(reader)
    column = ["first", "last", "house"]

#open the file to write in

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=column)
        writer.writeheader()
#Converts that input to that output, splitting each name into a first name and last name.
        for row in reader:
            name, house = row
            last, first = name.split(",")
#the name of a new CSV to write as output, whose columns should be, in order, first, last, and house
            writer.writerow({"first": first.strip(" "), "last": last, "house": house})