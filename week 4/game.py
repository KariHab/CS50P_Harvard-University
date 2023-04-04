import random


number = random.randint(0,100)
print(number)

try:
    while True:
        level = input("Level: ")
        if level.isnumeric() and level != "0":
            while True:
                guess = input("Guess: ")
                if guess.isnumeric() and guess != "0":
                    guess = int(guess)
                    if guess > number:
                        print("Too large!")

                    elif guess < number:
                        print("Too small!")

                    elif guess == number:
                        print("Just right!")
                        break
            break


except(ValueError):
    pass




