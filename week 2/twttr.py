def main():
    user_str = input("Input: ")
    n = shorten(user_str)
    print(f"Output: {n}")

def shorten(user_str):

    user_str = user_str.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
    user_str = user_str.replace("A", "").replace("E", "").replace("I", "").replace("O", "").replace("U", "")

    return user_str


if __name__ == "__main__":
    main()
