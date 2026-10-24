import operator
ops = {
    1: ("Addition", operator.add),
    2: ("Subtraction", operator.sub),
    3: ("Multiplication", operator.mul),
    4: ("Division", operator.truediv)
}
while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 5:
        print("Exiting the calculator")
        break
    if choice not in ops:
        print("Invalid choice")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 4 and b == 0:
        print("Division by zero is not possible")

    name, func = ops[choice]
    print(f"{name} = {func(a,b)}")