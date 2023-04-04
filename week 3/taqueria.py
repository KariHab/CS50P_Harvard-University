menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


total = 0

try:
    for item in menu:
        item = input("Item: ").title()

        if item in menu:
            total = total + menu[item]
            print(f'Total: ${total}0')
          
        if item.lower() == "control-d":
            break


except (KeyError, ValueError, EOFError, RuntimeError):
    pass
