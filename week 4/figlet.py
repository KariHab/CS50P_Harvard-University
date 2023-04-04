
import pyfiglet
import sys
import random


if len(sys.argv) == 1:
    user_text = input("Input: ")
    fonts = pyfiglet.FigletFont.getFonts()
    random_font = random.choices(fonts)
    random_font = " ".join(random_font)
    result = pyfiglet.figlet_format(user_text, font = random_font)
    print("Output: ", result)


if len(sys.argv) == 2 or len(sys.argv) == 3:
    fonts = pyfiglet.FigletFont.getFonts()
    if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in fonts:
        user_text = input("Input: ")
        result = pyfiglet.figlet_format(user_text, font = sys.argv[2])
        print("Output: ", result)

    else:
        sys.exit("Invalid usage")


