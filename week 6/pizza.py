import tabulate
from tabulate import tabulate
import sys
import os.path
from os import path
import csv


#one command-line argument, the name (or path) of a CSV
#if zero or more and 2 arg . sys exit
if len(sys.argv) < 2:
    sys.exit("Must enter a file name")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

#if file exist pas  - sys. exit
elif not path.exists(sys.argv[1]):
    sys.exit("File does not exist")

else:

    a,b = sys.argv[1].split(".")
    if b != "csv":
        sys.exit("not a csv file")

    if b == "csv" and len(sys.argv) == 2:

        with open(sys.argv[1]) as file:
            reader = csv.reader(file, delimiter = ",")
            headers = next(reader)

            mylines = []

            for row in reader:
                mylines.append(row)

            print(tabulate(mylines, headers, tablefmt="grid"))


