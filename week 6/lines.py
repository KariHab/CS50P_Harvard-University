import sys
import os.path
from os import path



#ask for a command line arg
name = sys.argv[1]
a,b = name.split(".")

if b != "py" or len(sys.argv) < 2 or len(sys.argv) > 2:
    sys.exit("does not meet the requirements")

elif not path.exists(sys.argv[1]):
    sys.exit()

else:
    with open(sys.argv[1], 'r') as file:
        lines = file.read().splitlines()
        count_lines = len(lines)
        blank = 0
        comment = 0
        for line in lines:
            verify = line.rstrip().strip().split('\n')
            for l in verify:
                if len(l) < 1:
                    blank += 1
                elif len(l) > 0 and l.startswith('#'):
                    comment += 1
        total = count_lines - blank - comment
        print(total)

