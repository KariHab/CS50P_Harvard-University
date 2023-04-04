paid = 0

while paid < 50:
    insert = int(input("Insert Coin: "))

    if insert == 25 or insert == 10 or insert == 5:
        paid = insert + paid

        if paid < 50:
            print("Amount Due: ", 50 - paid)

        if paid == 50:
            print("Change owed: ", 50 - paid)

        if paid > 50:
            print("Change owed: ", paid - 50)

    else:
            print(50)
            break
