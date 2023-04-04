while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        calculated = int(round((x / y) * 100))
        if calculated > 1 and calculated < 99:
            print(f'{calculated}%')
            break
        elif calculated <= 1:
            print("E")
            break
        elif calculated >= 99 and x<=y:
            print("F")
            break
    except (ValueError, ZeroDivisionError):
        pass
