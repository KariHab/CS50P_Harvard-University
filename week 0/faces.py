#implement a convert() accepts str as input and returns the same input with conversion
def convert():
    text = input()
    return text.replace(":)", "🙂").replace(":(", "🙁")



# implement main() ask user for input, calls convert and prints results
def main():
    print(convert())


main()
