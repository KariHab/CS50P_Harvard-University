def main():
    greeting = input("Greeting: ").lower().strip()
    n = value(greeting)
    print("$",n, sep="")


def value(greeting):
#if greeting = "hello" output 0$
    if (greeting.find("hello") != -1):
        #print("$0")
        return 0

#if greeting starts with "h" output $20
    elif greeting[0] == "h" and greeting != "hello":
        #print("$20")
        return 20

#otherwise output $100
    else:
        #print("$100")
        return 100


if __name__ == "__main__":
    main()






