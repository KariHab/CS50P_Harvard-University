# ask for an expression
calcul_user = input("Expression: ")

# split variable for the calculator
x, y, z = calcul_user.split(" ")

# transform into int for the calculator
x = int(x)
z = int(z)


if y == "+":
    calculator = float(x + z)
    print(calculator)
elif y == "*":
    calculator = float(x * z)
    print(calculator)
elif y == "/":

    calculator = float(x / z)
    print(calculator)
else:
    calculator = float(x - z)
    print(calculator)
