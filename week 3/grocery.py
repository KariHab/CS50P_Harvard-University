
grocery_list = {}

while True:
    try:
        item = input("").upper()
        if item in grocery_list:
            grocery_list[item] = grocery_list[item] + 1
        else:
            grocery_list[item] = 1

    except EOFError:
        if grocery_list == {}:
            break
        else:
            for i in sorted(grocery_list):
                print(grocery_list[i], i)
            break
