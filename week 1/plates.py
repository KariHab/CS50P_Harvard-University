def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    number = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    letter = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    if plate.startswith(number, 0, 2):
        return False
    elif len(plate) < 2 or len(plate) > 6:
        return False
    elif plate.isalnum() == False:
        return False
    elif plate[2] == "0" and plate[3:6] != "0":
        return False
    elif plate.startswith(number, 2,4) and plate.endswith(letter, 4,5):
        return False
    else:
        return True



main()








