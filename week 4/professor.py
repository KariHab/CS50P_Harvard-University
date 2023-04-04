import random

def main():
    level = get_level()

    error = 0
    score = 0
    for i in range (0, 10):
        x = generate_integer(level)
        y = generate_integer(level)
        problem = x + y
        for j in range (0,3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == problem:
                    error = 0
                    score +=1
                    break
                elif answer != problem:
                    error += 1
                    print("EEE")

                if error == 3:
                    print(f"{x} + {y} = {problem}")
                    break

            except ValueError:
                errors += 1
                print("EEE")


    print(f"Score: {score}")


def get_level():
    while True:
        level = input("Level: ")
        if level =="1" or level == "2" or level == "3":
            return int(level)


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    if level == 2:
        return random.randint(10,99)
    if level == 3:
        return random.randint(100,999)
    if level <1 or level >3:
        raise ValueError



if __name__ == "__main__":
    main()





