#Study buddy - January 2023 - Karima Habbout

import csv
import random
def main():
    starting = input("What do you want to do? Test [T] / Add [A]: ")
    if starting == "T":
        test()
    elif starting == "A":
        get_questions()


def get_questions():
    number_question = input("How many questions you would like to enter? ")
    print(number_question)

def store_questions():
    ...


def number():
    questions_set = input("How many questions would you like to practice today?")
    print(questions_set)
    return questions_set
def test():
    print("Let's start the test...Take your time to recall as much as possible")




if __name__ == '__main__':
    main()